from datetime import datetime
import xml.etree.ElementTree as ET

import logfire
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import Response

from . import logger
from .Contact import contact_test


# TODO: Implement GET, PUT, DELETE methods


async def get_vcard(request: Request):
    # logger.debug(f"Method '{request.method}'")
    # logger.debug(f"Path '{request.path_params}'")
    # logger.debug(f"Query params '{request.query_params}'")
    vcard_data = contact_test.toVcard()
    card_id = request.path_params.get("card_id", "")
    logger.info(f"Got card id {card_id}")
    return Response(
        content=vcard_data,
        headers={
            "Content-Type": "text/vcard; charset=utf-8",
            "Content-Length": str(len(vcard_data)),
        },
    )


async def get_options(request: Request):
    return Response(
        headers={
            "Allow": "OPTIONS, GET, PUT, DELETE, PROPFIND, REPORT",
            "DAV": "1, 3, addressbook",
            "Content-Length": "0",
        },
    )


async def get_props(request: Request):
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

        _list_vcards = [("1", 123)]
        for vcard_id, vcard_len in _list_vcards:
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
        Route("/{card_id}", get_vcard, methods=["GET"]),
        Route("/", get_options, methods=["OPTIONS"]),
        Route("/", get_props, methods=["PROPFIND"]),
    ]
)

logfire.instrument_starlette(app)
