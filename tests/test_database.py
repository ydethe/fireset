from datetime import datetime
from hypothesis import given, strategies as st

from fireset.store.Contact import Contact, Adresse, Email, Telephone


@given(adresse=st.builds(Adresse), nb_item=st.integers())
def test_adresses(adresse: Adresse, nb_item: int):
    vcf = adresse.toVcard(nb_item)
    new = Adresse.fromVcard(vcf)

    assert new == adresse


@given(email=st.builds(Email), nb_item=st.integers())
def test_emails(email: Email, nb_item: int):
    if email.email == "":
        return

    vcf = email.toVcard(nb_item)
    new = Email.fromVcard(vcf)

    assert new == email


@given(telephone=st.builds(Telephone), nb_item=st.integers())
def test_telephones(telephone: Telephone, nb_item: int):
    if telephone.telephone == "":
        return

    vcf = telephone.toVcard(nb_item)
    new = Telephone.fromVcard(vcf)

    assert new == telephone


@given(contact=st.builds(Contact))
def test_contacts(contact: Contact):
    if contact.date_naissance.year < datetime.now().year - 200:
        return

    if contact.nom_de_naissance != "":
        return

    for tel in contact.telephones:
        if tel.telephone == "":
            return

    for email in contact.emails:
        if email.email == "":
            return

    # https://stackoverflow.com/questions/70396266/how-to-generate-test-samples-with-hypothesis-directly-from-dataclasses
    vcf = contact.toVcard()
    new = Contact.fromVcard([vcf])

    assert new == contact


if __name__ == "__main__":
    # from fireset.store.Contact import contact_test

    # vcf = contact_test.toVcard()
    # new = Contact.fromVcard([vcf])

    # assert new == contact_test

    # test_adresses()
    # test_emails()
    # test_telephones()
    test_contacts()
