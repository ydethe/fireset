from dataclasses import dataclass
from datetime import datetime
import typing as T

from . import settings


@dataclass
class Adresse:
    id: int
    boite_postale: str
    adresse_etendue: str
    rue: str
    ville: str
    region: str
    code_postal: str
    pays: str
    telephone: str
    type: str
    prefered: bool


@dataclass
class Email:
    id: int
    email: str
    type: str
    prefered: bool


@dataclass
class Telephone:
    id: int
    telephone: str
    type: str
    prefered: bool


@dataclass
class Contact:
    id: int
    organisation: str
    fonction: str
    nom: str
    prenom: str
    website: str
    date_naissance: datetime
    nom_de_naissance: str
    civilite: str
    linkedin_profil: str
    notes: str
    photo: bytes
    adresses: T.List[Adresse]
    emails: T.List[Email]
    telephones: T.List[Telephone]

    def toVcard(self) -> bytes:
        res = b""

        res += b"BEGIN:VCARD\n"
        res += b"VERSION:3.0\n"
        res += f"N:{self.nom};{self.prenom};;{self.civilite};\n".encode(encoding="utf-8")
        res += f"FN:{self.prenom} {self.nom}\n".encode(encoding="utf-8")
        if self.date_naissance.year > 1:
            res += f"BDAY;VALUE=date:{self.date_naissance:%Y-%m-%d}\n".encode(encoding="utf-8")
        if len(self.photo) > 0:
            res += b"PHOTO:data:image/jpeg;base64," + self.photo + b"\n"
        if len(self.organisation) > 0:
            res += f"ORG:{self.organisation};\n".encode(encoding="utf-8")
        if len(self.fonction) > 0:
            res += f"TITLE:{self.fonction}\n".encode(encoding="utf-8")
        if len(self.notes) > 0:
            res += f"NOTE:{self.notes}\n".encode(encoding="utf-8")
        # res += f"GENDER:{F}\n".encode(encoding="utf-8")

        nb_item = 1
        for adresse in self.adresses:
            if adresse.prefered:
                pref_str = ";TYPE=pref"
            else:
                pref_str = ""
            res += f"item{nb_item}.ADR{pref_str}:{adresse.boite_postale};{adresse.adresse_etendue};{adresse.rue};{adresse.ville};{adresse.region};{adresse.code_postal};{adresse.pays}\n".encode(
                encoding="utf-8"
            )
            res += f"item{nb_item}.X-ABLABEL:{adresse.type}\n".encode(encoding="utf-8")
            res += f"item{nb_item}.X-ABADR:fr\n".encode(encoding="utf-8")
            nb_item += 1

        for telephone in self.telephones:
            if telephone.prefered:
                pref_str = ";TYPE=pref"
            else:
                pref_str = ""
            res += f"item{nb_item}.TEL{pref_str}:{telephone.telephone}\n".encode(encoding="utf-8")
            res += f"item{nb_item}.X-ABLABEL:{telephone.type}\n".encode(encoding="utf-8")
            nb_item += 1

        if len(self.website) > 0:
            res += f"item{nb_item}.URL:{self.website}\n".encode(encoding="utf-8")
            res += f"item{nb_item}.X-ABLABEL:_$!<HomePage>!$_\n".encode(encoding="utf-8")
            nb_item += 1

        res += f"item{nb_item}.URL;TYPE=pref:{settings.server_url}{self.id}\n".encode(
            encoding="utf-8"
        )
        res += f"item{nb_item}.X-ABLABEL:_$!<ProfilePage>!$_\n".encode(encoding="utf-8")
        nb_item += 1

        for email in self.emails:
            if email.prefered:
                pref_str = ";TYPE=pref"
            else:
                pref_str = ""
            res += f"item{nb_item}.EMAIL{pref_str};TYPE=INTERNET:{email.email}\n".encode(
                encoding="utf-8"
            )
            res += f"item{nb_item}.X-ABLABEL:{email.type}\n".encode(encoding="utf-8")
            nb_item += 1

        if len(self.linkedin_profil) > 0:
            elem = self.linkedin_profil.split("/")
            while "" in elem:
                elem.remove("")
            user = elem[-1]
            res += f"X-SOCIALPROFILE;X-USER={user};TYPE=linkedin:{self.linkedin_profil}\n".encode(
                encoding="utf-8"
            )
        res += b"PRODID:fireset\n"
        res += b"END:VCARD\n"

        return res


contact_test = Contact(
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
            prefered=True,
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
            prefered=False,
        ),
    ],
    emails=[
        Email(id=1, email="chantal.goya@gmail.com", type="type1", prefered=True),
        Email(id=2, email="chantal.goya@olympia.fr", type="type2", prefered=False),
        Email(id=3, email="chantal.goya@cours-florent-alumni.com", type="type3", prefered=False),
    ],
    telephones=[
        Telephone(id=1, telephone="+33 6 98 76 54 32", type="type1", prefered=True),
        Telephone(id=2, telephone="+33 1 23 45 67 89", type="type2", prefered=False),
    ],
)
