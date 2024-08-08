# List vCards::

#     curl http://localhost:8901/

# Upload a vCard::

#     curl -X PUT --data-binary @contact.vcf http://localhost:8901/johndoe

# Download a vCard::

#     curl http://localhost:8901/johndoe

from fireset.app import run


def test_server():
    run()


if __name__ == "__main__":
    test_server()
