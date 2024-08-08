# List vCards::

#     curl http://localhost:8901/

# Upload a vCard::

#     curl -X PUT --data-binary @contact.vcf http://localhost:8901/johndoe

# Download a vCard::

#     curl http://localhost:8901/johndoe

from fireset.server import app


def test_server():
    import uvicorn

    uvicorn.run(app, port=8901)


if __name__ == "__main__":
    test_server()
