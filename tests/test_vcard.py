import logfire

from fireset.Contact import contact_test


def test_vcard():
    data = contact_test.toVcard()
    with open("tests/generated.vcf", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    test_vcard()
    logfire.info("Test done: {name}", name="test_vcard")
