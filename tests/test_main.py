import asyncio
import functools
import logging
import os
import socket

from aiohttp_basicauth_middleware import basic_auth_middleware

from fireset import settings
from fireset.web import (
    WELLKNOWN_DAV_PATHS,
    RedirectDavHandler,
    XandikosApp,
    XandikosBackend,
    avahi_register,
)

try:
    from asyncio import to_thread  # type: ignore
except ImportError:  # python < 3.8
    import contextvars
    from asyncio import events

    async def to_thread(func, *args, **kwargs):  # type: ignore
        loop = events.get_running_loop()
        ctx = contextvars.copy_context()
        func_call = functools.partial(ctx.run, func, *args, **kwargs)
        return await loop.run_in_executor(None, func_call)


try:
    import systemd.daemon
except ImportError:
    systemd_imported = False

    def get_systemd_listen_sockets() -> list[socket.socket]:
        raise NotImplementedError

else:
    systemd_imported = True

    def get_systemd_listen_sockets() -> list[socket.socket]:
        socks = []
        for fd in systemd.daemon.listen_fds():
            for family in (
                socket.AF_UNIX,  # type: ignore
                socket.AF_INET,
                socket.AF_INET6,
            ):
                if systemd.daemon.is_socket(
                    fd, family=family, type=socket.SOCK_STREAM, listening=True
                ):
                    sock = socket.fromfd(fd, family, socket.SOCK_STREAM)
                    socks.append(sock)
                    break
            else:
                raise RuntimeError(
                    "socket family must be AF_INET, AF_INET6, or AF_UNIX; "
                    "socket type must be SOCK_STREAM; and it must be listening"
                )
        return socks


logger = logging.getLogger("fireset_logger")


async def main_for_test():
    directory = "data"
    paranoid = False
    index_threshold = None
    current_user_principal = "user"
    autocreate = True
    defaults = True
    strict = False
    route_prefix = "/"
    detect_systemd = False
    listen_address = "0.0.0.0"
    port = 8000
    metrics_port = 8001
    avahi = True

    backend = XandikosBackend(
        os.path.abspath(directory),
        paranoid=paranoid,
        index_threshold=index_threshold,
    )
    backend._mark_as_principal(current_user_principal)

    if autocreate or defaults:
        if not os.path.isdir(directory):
            os.makedirs(directory)
        backend.create_principal(current_user_principal, create_defaults=defaults)

    if not os.path.isdir(directory):
        logger.warning(
            "%r does not exist. Run fireset with --autocreate?",
            directory,
        )
    if not backend.get_resource(current_user_principal):
        logger.warning(
            "default user principal %s does not exist. " "Run fireset with --autocreate?",
            current_user_principal,
        )

    main_app = XandikosApp(
        backend,
        current_user_principal=current_user_principal,
        strict=strict,
    )

    async def xandikos_handler(request):
        return await main_app.aiohttp_handler(request, route_prefix)

    if detect_systemd and not systemd_imported:
        logger.error("systemd detection requested, but unable to find systemd_python")

    if detect_systemd and systemd.daemon.booted():
        listen_socks = get_systemd_listen_sockets()
        socket_path = None
        listen_address = None
        listen_port = None
        logger.info("Receiving file descriptors from systemd socket activation")
    elif "/" in listen_address:
        socket_path = listen_address
        listen_address = None
        listen_port = None  # otherwise aiohttp also listens on default host
        listen_socks = []
        logger.info("Listening on unix domain socket %s", socket_path)
    else:
        listen_address = listen_address
        listen_port = port
        socket_path = None
        listen_socks = []
        logger.info("Listening on %s:%s", listen_address, port)

    from aiohttp import web

    if metrics_port == port:
        logger.error("Metrics port cannot be the same as the main port")

    app = web.Application()

    logger.info(f"Added auth for user '{settings.fireset_user}'")

    app.middlewares.append(
        basic_auth_middleware(
            ("/",),
            {settings.fireset_user: settings.fireset_password},
        )
    )

    if metrics_port:
        metrics_app = web.Application()
        try:
            from aiohttp_openmetrics import metrics, metrics_middleware
        except ModuleNotFoundError:
            logger.warning("aiohttp-openmetrics not found; " "/metrics will not be available.")
        else:
            app.middlewares.insert(0, metrics_middleware)
            metrics_app.router.add_get("/metrics", metrics, name="metrics")

        # For now, just always claim everything is okay.
        metrics_app.router.add_get("/health", lambda r: web.Response(text="ok"))
    else:
        metrics_app = None

    for path in WELLKNOWN_DAV_PATHS:
        app.router.add_route("*", path, RedirectDavHandler(route_prefix).__call__)

    if route_prefix.strip("/"):
        xandikos_app = web.Application()
        xandikos_app.router.add_route("*", "/{path_info:.*}", xandikos_handler)

        async def redirect_to_subprefix(request):
            return web.HTTPFound(route_prefix)

        app.router.add_route("*", "/", redirect_to_subprefix)
        app.add_subapp(route_prefix, xandikos_app)
    else:
        app.router.add_route("*", "/{path_info:.*}", xandikos_handler)

    if avahi:
        try:
            import avahi  # noqa: F401
            import dbus  # noqa: F401
        except ImportError:
            logger.error("Please install python-avahi and python-dbus for " "avahi support.")
        else:
            avahi_register(port, route_prefix)

    runner = web.AppRunner(app)
    await runner.setup()
    sites = []
    if metrics_app:
        metrics_runner = web.AppRunner(metrics_app)
        await metrics_runner.setup()
        # TODO(jelmer): Allow different metrics listen addres?
        sites.append(web.TCPSite(metrics_runner, listen_address, metrics_port))
    # Use systemd sockets first and only if not present use the socket path or
    # address from --listen-address.
    if listen_socks:
        sites.extend([web.SockSite(runner, sock) for sock in listen_socks])
    elif socket_path:
        sites.append(web.UnixSite(runner, socket_path))
    else:
        sites.append(web.TCPSite(runner, listen_address, listen_port))

    import signal

    # Set SIGINT to default handler; this appears to be necessary
    # when running under coverage.
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    for site in sites:
        await site.start()

    while True:
        await asyncio.sleep(3600)


def test_main():
    return asyncio.run(main_for_test())
