from datetime import datetime
import xml.etree.ElementTree as ET

import logfire
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import Response, PlainTextResponse
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

from . import logger, settings
from .database import get_db_vcard, list_db_vcards
from .authentication import BasicAuth, authenticated, FiresetUser


@authenticated
async def handle_card_get(request: Request):
    user: FiresetUser = request.user
    user_id = int(request.path_params.get("user_id", -1))
    assert user.id == user_id

    # logger.debug(f"Method '{request.method}'")
    # logger.debug(f"Path '{request.path_params}'")
    # logger.debug(f"Query params '{request.query_params}'")

    card_id = int(request.path_params.get("card_id", -1))

    contact = get_db_vcard(card_id)
    if contact is None:
        return Response(status_code=400)

    vcard_data = contact.toVcard()

    return Response(
        content=vcard_data,
        headers={
            "Content-Type": "text/vcard; charset=utf-8",
            "Content-Length": str(len(vcard_data)),
        },
    )


@authenticated
async def handle_users_options(request: Request):
    return Response(
        headers={
            "Allow": "OPTIONS, GET, PUT, DELETE, PROPFIND, REPORT",
            "DAV": "1, 2, addressbook",
            "Content-Length": "0",
        },
    )


@authenticated
async def handle_users_propfind(request: Request):
    user: FiresetUser = request.user

    depth = request.headers.get("Depth", "0")
    content_length = int(request.headers.get("Content-Length", 0))
    request_body = await request.body()

    if content_length > 0:
        try:
            # Parse the XML request
            root = ET.fromstring(request_body)
            namespace = {"D": "DAV:"}
            propfind = root.find("D:prop", namespace)
        except ET.ParseError:
            return Response(status_code=400)
    else:
        propfind = None

    logger.info(f"propfind: {propfind}")

    if depth == "0":
        # Listing collections
        response = '<?xml version="1.0" encoding="UTF-8"?>\n'
        response += '<D:multistatus xmlns:D="DAV:" xmlns:C="urn:ietf:params:xml:ns:carddav">\n'
        response += "  <D:response>\n"
        response += f"    <D:href>/users/{user.id}</D:href>\n"
        response += "    <D:propstat>\n"
        response += "      <D:prop>\n"
        response += "        <D:resourcetype>\n"
        response += "          <D:collection/>\n"
        response += "        </D:resourcetype>\n"
        response += "        <D:displayname>vCards</D:displayname>\n"
        response += "      </D:prop>\n"
        response += "      <D:status>HTTP/1.1 200 OK</D:status>\n"
        response += "    </D:propstat>\n"
        response += "  </D:response>\n"
        response += "</D:multistatus>"

        return Response(
            status_code=207,
            headers={"Content-Type": 'application/xml; charset="utf-8"'},
            content=response.encode("utf-8"),
        )

    elif depth == "1":
        # Listing resources within collections
        response = '<?xml version="1.0" encoding="UTF-8"?>\n'
        response += '<D:multistatus xmlns:D="DAV:">\n'

        for vcard in list_db_vcards():
            vcard_id = vcard.id
            vcard_len = 100

            response += "  <D:response>\n"
            response += f"    <D:href>/{vcard_id}</D:href>\n"
            response += "    <D:propstat>\n"
            response += "      <D:prop>\n"
            response += "        <D:resourcetype/>\n"
            response += f"        <D:displayname>{vcard_id}</D:displayname>\n"
            response += "        <D:getcontenttype>text/vcard</D:getcontenttype>\n"
            response += f"        <D:getcontentlength>{vcard_len}</D:getcontentlength>\n"
            response += f'        <D:getetag>"{vcard_id}"</D:getetag>\n'
            response += "        <D:getlastmodified>{}</D:getlastmodified>\n".format(
                datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
            )
            response += "      </D:prop>\n"
            response += "      <D:status>HTTP/1.1 200 OK</D:status>\n"
            response += "    </D:propstat>\n"
            response += "  </D:response>\n"

        response += "</D:multistatus>"

        return Response(
            status_code=207,
            headers={"Content-Type": 'application/xml; charset="utf-8"'},
            content=response.encode("utf-8"),
        )

    else:
        return Response(status_code=400)


@authenticated
async def handle_wall_known(request: Request):
    user: FiresetUser = request.user
    return Response(
        status_code=302, headers={"Location": f"{settings.server_url}/users/{user.id}/"}
    )


@authenticated
async def handle_addressbooks_options(request: Request):
    return Response(
        headers={
            "Allow": "OPTIONS, PROPFIND, REPORT",
            "DAV": "1, 2, addressbook",
        },
    )


@authenticated
async def handle_addressbooks_propfind(request: Request):
    user: FiresetUser = request.user

    depth = request.headers.get("Depth", "0")
    content_length = int(request.headers.get("Content-Length", 0))
    request_body = await request.body()

    if content_length > 0:
        try:
            # Parse the XML request
            root = ET.fromstring(request_body)
            namespace = {"D": "DAV:"}
            propfind = root.find("D:prop", namespace)
        except ET.ParseError:
            return Response(status_code=400)
    else:
        propfind = None

    logger.info(f"propfind: {propfind}")

    if depth == "1":
        # Listing resources within collections
        response = '<?xml version="1.0" encoding="UTF-8"?>\n'
        response += '<D:multistatus xmlns:D="DAV:" xmlns:C="urn:ietf:params:xml:ns:carddav">\n'
        response += "  <D:response>\n"
        response += f"    <D:href>/users/{user.id}/addressbooks/main</D:href>\n"
        response += "    <D:propstat>\n"
        response += "      <D:prop>\n"
        response += "        <D:displayname>Contacts</D:displayname>\n"
        response += "        <C:addressbook-description>Contacts</C:addressbook-description>\n"
        response += "      </D:prop>\n"
        response += "      <D:status>HTTP/1.1 200 OK</D:status>\n"
        response += "    </D:propstat>\n"
        response += "  </D:response>\n"
        response += "</D:multistatus>"

        return Response(
            status_code=207,
            headers={"Content-Type": 'application/xml; charset="utf-8"'},
            content=response.encode("utf-8"),
        )

    else:
        return Response(status_code=400)


app = Starlette(
    routes=[
        Route("/.well-known/carddav", handle_wall_known, methods=["GET"]),
        Route("/", handle_users_propfind, methods=["PROPFIND"]),
        Route("/principals", handle_users_propfind, methods=["PROPFIND"]),
        Route("/users/{user_id}", handle_users_propfind, methods=["PROPFIND"]),
        Route("/users/{user_id}", handle_users_options, methods=["OPTIONS"]),
        Route("/users/{user_id}/addressbooks", handle_addressbooks_propfind, methods=["PROPFIND"]),
        Route("/users/{user_id}/addressbooks", handle_addressbooks_options, methods=["OPTIONS"]),
        Route(
            "/users/{user_id}/addressbooks/{addressbook_id}/{card_id}.vcf",
            handle_card_get,
            methods=["GET"],
        ),
    ],
    middleware=[
        Middleware(
            AuthenticationMiddleware,
            backend=BasicAuth(),
            on_error=lambda _, exc: PlainTextResponse(str(exc), status_code=401),
        )
    ],
)

logfire.instrument_starlette(app)
