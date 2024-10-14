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
    # new = Contact.fromVcard([vcf])

    # assert new == contact_test

    from parse import Parser

    # fmt = "SOURCE:adr:{aid:d}\nitem{nb_item:d}.ADR{pref_str}:{boite_postale};{adresse_etendue};{rue};{ville};{region};{code_postal};{pays}\nitem{nb_item:d}.X-ABLABEL:{type}"
    # v = "SOURCE:adr:1\nitem1.ADR;TYPE=pref:;;12 rue Chauvelot;Paris;;75015;France\nitem1.X-ABLABEL:type1"

    fmt = "SOURCE:adr:{aid:d}\nitem{nb_item:d}.ADR{pref_str}:{elems}\nitem{nb_item:d}.X-ABLABEL:{type}"
    v = "SOURCE:adr:1\nitem1.ADR;TYPE=pref:;;12 rue Chauvelot;Paris;;75015;France\nitem1.X-ABLABEL:type1"

    p = Parser(fmt)
    res = p.parse(fmt, v)
    print(res)
