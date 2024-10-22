from uuid import UUID
from starlette.applications import Starlette
from starlette.responses import Response
from starlette.routing import Route
from starlette.requests import Request

from xml.etree import ElementTree as ET

from fireset.store import db_connection
from fireset.webdav import (
    _send_not_found,
    _readXmlBody,
    _send_simple_dav_error,
)
from fireset import logger


async def handle_report(request: Request):
    # See https://tools.ietf.org/html/rfc3253, section 3.6
    base_href, unused_path, r = app._get_resource_from_environ(request)
    if r is None:
        return _send_not_found(request)

    # depth = request.headers.get("Depth", "0")
    et = await _readXmlBody(request, None, strict=app.strict)

    try:
        reporter = app.reporters[et.tag]
    except KeyError:
        logger.warning("Client requested unknown REPORT %s", et.tag)
        return _send_simple_dav_error(
            request,
            "403 Forbidden",
            error=ET.Element("{DAV:}supported-report"),
            description=f"Unknown report {et.tag}.",
        )

    if not reporter.supported_on(r):
        return _send_simple_dav_error(
            request,
            "403 Forbidden",
            error=ET.Element("{DAV:}supported-report"),
            description=f"Report {et.tag} not supported on resource.",
        )

    # try:
    #     return await reporter.report(
    #         environ,
    #         et,
    #         functools.partial(_get_resources_by_hrefs, app.backend, environ),
    #         app.properties,
    #         base_href,
    #         r,
    #         depth,
    #         app.strict,
    #     )
    # except PreconditionFailure as e:
    #     return _send_simple_dav_error(
    #         request,
    #         "412 Precondition Failed",
    #         error=ET.Element(e.precondition),
    #         description=e.description,
    #     )


async def do_get(request: Request, send_body: bool):
    path: str = request.path_params["path"]
    if path.endswith(".vcf"):
        name = path.split("/")[-1]
        current_etag = name.split(".")[0]
        content_type = "text/vcard"
        content_languages = []
        vcard = db_connection.get_db_vcard_by_etag(UUID(current_etag))
        body = vcard.toVcard()
    else:
        current_etag = None
        content_type = None
        content_languages = []
        body = b""

    content_length = len(body)

    # if_none_match = request.headers.get("If-None-Match", None)

    # if if_none_match and current_etag is not None and etag_matches(if_none_match, current_etag):
    #     return Response(status="304 Not Modified")

    headers = {"Content-Length": str(content_length)}

    if current_etag is not None:
        headers["ETag"] = current_etag

    if content_type is not None:
        headers["Content-Type"] = content_type

    # try:
    #     last_modified = r.get_last_modified()
    # except KeyError:
    #     pass
    # else:
    #     headers["Last-Modified"] = last_modified

    if content_languages is not None:
        headers["Content-Language"] = ", ".join(content_languages)

    if send_body:
        return Response(content=body, status_code=200, headers=headers)
    else:
        return Response(status_code=200, headers=headers)


async def handle_get(request: Request):
    return await do_get(request, send_body=True)


routes = [
    Route(path="/{path:path}", endpoint=handle_get, methods=["GET"]),
    Route(path="/{path:path}", endpoint=handle_report, methods=["REPORT"]),
]
app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
