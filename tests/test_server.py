# List vCards::

#     curl http://localhost:8000/

# Upload a vCard::

#     curl -X PUT --data-binary @contact.vcf http://localhost:8000/52

# Download a vCard::

#     curl http://localhost:8000/52

from fireset.server import app


def test_server():
    import uvicorn

    uvicorn.run(app, port=8000)


if __name__ == "__main__":
    test_server()
