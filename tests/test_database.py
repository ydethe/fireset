from hypothesis import given
from hypothesis.strategies import from_type

from fireset.store.Contact import Contact


@given(contact=from_type(Contact))
def test_contacts(contact: Contact):
    # https://stackoverflow.com/questions/70396266/how-to-generate-test-samples-with-hypothesis-directly-from-dataclasses
    vcf = contact.toVcard()
    new = Contact.fromVcard([vcf])

    assert new == contact


if __name__ == "__main__":
    from fireset.store.Contact import contact_test

    vcf = contact_test.toVcard()
    new = Contact.fromVcard([vcf])

    assert new == contact_test
