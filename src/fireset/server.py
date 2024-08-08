from fastapi import FastAPI, Response

from .Configuration import logfire


app = FastAPI()

logfire.instrument_fastapi(app)


@app.get("/{card_id}", status_code=200)
async def hello(card_id):
    vcard_data = b"poney"
    return Response(
        content=vcard_data,
        headers={
            "Content-Type": "text/vcard; charset=utf-8",
            "Content-Length": str(len(vcard_data)),
        },
    )
