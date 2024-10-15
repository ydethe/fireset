from hypothesis.strategies import from_type
from hypothesis import given, strategies as st

from fireset.store.Contact import Contact, Adresse, Email, Telephone


@given(contact=from_type(Contact))
def test_contacts(contact: Contact):
    # https://stackoverflow.com/questions/70396266/how-to-generate-test-samples-with-hypothesis-directly-from-dataclasses
    vcf = contact.toVcard()
    new = Contact.fromVcard([vcf])

    assert new == contact


@given(adresse=from_type(Adresse), nb_item=st.integers())
def test_adresses(adresse: Adresse, nb_item: int):
    vcf = adresse.toVcard(nb_item)
    new = Adresse.fromVcard(vcf)

    assert new == adresse


@given(email=from_type(Email), nb_item=st.integers())
def test_emails(email: Email, nb_item: int):
    if email.email == "":
        return

    vcf = email.toVcard(nb_item)
    new = Email.fromVcard(vcf)

    assert new == email


@given(telephone=from_type(Telephone), nb_item=st.integers())
def test_telephones(telephone: Telephone, nb_item: int):
    if telephone.telephone == "":
        return

    vcf = telephone.toVcard(nb_item)
    new = Telephone.fromVcard(vcf)

    assert new == telephone


if __name__ == "__main__":
    # from fireset.store.Contact import contact_test

    # vcf = contact_test.toVcard()
    # new = Contact.fromVcard([vcf])

    # assert new == contact_test

    test_adresses()
    test_emails()
    test_telephones()
