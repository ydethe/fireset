import logfire
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import Response

from . import logger
from .Contact import contact_test


async def get_vcard(request: Request):
    # logger.debug(f"[DEBUG] Method '{request.method}'")
    # logger.debug(f"[DEBUG] Path '{request.path_params}'")
    # logger.debug(f"[DEBUG] Query params '{request.query_params}'")
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


async def get_props(request: Request):
    return Response(
        headers={
            "Allow": "OPTIONS, GET, PUT, DELETE, PROPFIND, REPORT",
            "DAV": "1, 3, addressbook",
            "Content-Length": "0",
        },
    )


app = Starlette(
    routes=[
        Route("/{card_id}", get_vcard, methods=["GET"]),
        Route("/", get_props, methods=["PROPFIND"]),
    ]
)

logfire.instrument_starlette(app)
