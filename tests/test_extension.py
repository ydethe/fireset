# List vCards::

#     curl http://localhost:8000/

# Upload a vCard::

#     curl -X PUT --data-binary @contact.vcf http://localhost:8000/johndoe

# Download a vCard::

#     curl http://localhost:8000/johndoe


def test_py():
    from fireset.compute import python_add

    assert python_add(2, 3) == 5


if __name__ == "__main__":

    test_py()
