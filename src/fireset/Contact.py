from dataclasses import dataclass
from datetime import datetime
import typing as T


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


@dataclass
class Email:
    email: str
    type: str


@dataclass
class Telephone:
    telephone: str
    type: str


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
        res += f"BDAY;VALUE=date:{self.date_naissance:%Y-%m-%d}\n".encode(encoding="utf-8")
        res += b"PHOTO:data:image/jpeg;base64," + self.photo + b"\n"
        res += f"ORG:{self.organisation};\n".encode(encoding="utf-8")
        res += f"TITLE:{self.fonction}\n".encode(encoding="utf-8")
        res += f"NOTE:{self.notes}\n".encode(encoding="utf-8")
        # res += f"GENDER:{F}\n".encode(encoding="utf-8")
        nb_item = 1
        for adresse in self.adresses:
            res += f"item{nb_item}.ADR;TYPE=pref:{adresse.boite_postale};{adresse.adresse_etendue};{adresse.rue};{adresse.ville};{adresse.region};{adresse.code_postal};{adresse.pays}\n".encode(
                encoding="utf-8"
            )
            res += f"item{nb_item}.X-ABLABEL:{adresse.type}\n".encode(encoding="utf-8")
            res += f"item{nb_item}.X-ABADR:fr\n".encode(encoding="utf-8")
            nb_item += 1
        for telephone in self.telephones:
            res += f"item{nb_item}.TEL;TYPE=pref:{telephone.telephone}\n".encode(encoding="utf-8")
            res += f"item{nb_item}.X-ABLABEL:{telephone.type}\n".encode(encoding="utf-8")
            nb_item += 1
        res += f"item3.URL;TYPE=pref:{self.website}\n".encode(encoding="utf-8")
        res += b"item3.X-ABLABEL:_$!<HomePage>!$_\n"
        for email in self.emails:
            res += f"item{nb_item}.EMAIL;TYPE=pref;TYPE=INTERNET:{email.email}\n".encode(
                encoding="utf-8"
            )
            res += f"item{nb_item}.X-ABLABEL:{email.type}\n".encode(encoding="utf-8")
            nb_item += 1
        res += f"X-SOCIALPROFILE;X-USER={self.linkedin_profil};TYPE=linkedin:https://www.linkedin.com/in/{self.linkedin_profil}\n".encode(
            encoding="utf-8"
        )
        res += b"PRODID:fireset\n"
        res += b"END:VCARD"

        return res
