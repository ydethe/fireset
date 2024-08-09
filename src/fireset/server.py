from dataclasses import dataclass
from datetime import datetime
import xml.etree.ElementTree as ET

import logfire
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import Response, PlainTextResponse
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette_auth_toolkit.base.backends import BaseBasicAuth
from starlette_auth_toolkit.cryptography import PBKDF2Hasher

from . import logger
from .database import get_db_vcard, list_db_vcards, get_contact_from_email


# Password hasher
hasher = PBKDF2Hasher()


@dataclass
class BookUser:
    email: str
    password: str
    is_authenticated: bool

    @classmethod
    def from_db(cls, email: str) -> "BookUser":
        db_contact = get_contact_from_email(email)
        if db_contact is None:
            return None

        if db_contact.hashed_password is None:
            return None

        res = cls(email=email, password=db_contact.hashed_password, is_authenticated=False)

        return res


# Authentication backend
class BasicAuth(BaseBasicAuth):
    async def find_user(self, username: str):
        u = BookUser.from_db(email=username)
        return u

    async def verify_password(self, user: BookUser, password: str):
        user.is_authenticated = await hasher.verify(password, user.password)
        return user.is_authenticated


async def handle_get(request: Request):
    # logger.debug(f"Method '{request.method}'")
    # logger.debug(f"Path '{request.path_params}'")
    # logger.debug(f"Query params '{request.query_params}'")
    if not request.user.is_authenticated:
        return Response(status_code=401)

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


async def handle_options(request: Request):
    if not request.user.is_authenticated:
        return Response(status_code=401)

    return Response(
        headers={
            "Allow": "OPTIONS, GET, PUT, DELETE, PROPFIND, REPORT",
            "DAV": "1, 3, addressbook",
            "Content-Length": "0",
        },
    )


async def handle_propfind(request: Request):
    if not request.user.is_authenticated:
        return Response(status_code=401)

    depth = request.headers.get("Depth", "0")
    content_length = int(request.headers.get("Content-Length", 0))
    request_body = await request.body()
    # request_body = self.rfile.read(content_length)
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

    logger.debug(f"{propfind}")

    if depth == "0":
        # Listing collections
        response = '<?xml version="1.0" encoding="UTF-8"?>\n'
        response += '<D:multistatus xmlns:D="DAV:">\n'
        response += "  <D:response>\n"
        response += "    <D:href>/</D:href>\n"
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


app = Starlette(
    routes=[
        Route("/{card_id}", handle_get, methods=["GET"]),
        Route("/", handle_options, methods=["OPTIONS"]),
        Route("/", handle_propfind, methods=["PROPFIND"]),
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
