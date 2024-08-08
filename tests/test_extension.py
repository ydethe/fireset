# List vCards::

#     curl http://localhost:8000/

# Upload a vCard::

#     curl -X PUT --data-binary @contact.vcf http://localhost:8000/johndoe

# Download a vCard::

#     curl http://localhost:8000/johndoe

from datetime import datetime
from fireset.Contact import Contact, Telephone, Email, Adresse


def test_vcard():
    contact = Contact(
        id=1,
        organisation="Opera Production",
        fonction="Chanteuse",
        nom="Goya",
        prenom="Chantal",
        website="https://home.domain.tld",
        date_naissance=datetime(1942, 6, 10),
        nom_de_naissance="",
        civilite="Mme",
        linkedin_profil="chantalgoya",
        notes="Notes",
        photo=b"",
        adresses=[
            Adresse(
                id=1,
                boite_postale="",
                adresse_etendue="",
                rue="12 rue Chauvelot",
                ville="Paris",
                region="",
                code_postal="75015",
                pays="France",
                telephone="",
                type="type1",
            ),
            Adresse(
                id=2,
                boite_postale="",
                adresse_etendue="",
                rue="1 rue de la Paix",
                ville="Paris",
                region="",
                code_postal="75008",
                pays="France",
                telephone="",
                type="type2",
            ),
        ],
        emails=[
            Email(email="chantal.goya@gmail.com", type="type1"),
            Email(email="chantal.goya@olympia.fr", type="type2"),
            Email(email="chantal.goya@cours-florent-alumni.com", type="type3"),
        ],
        telephones=[
            Telephone(telephone="+33 6 98 76 54 32", type="type1"),
            Telephone(telephone="+33 1 23 45 67 89", type="type2"),
        ],
    )

    print(contact.toVcard().decode("utf-8"))


if __name__ == "__main__":

    test_vcard()
