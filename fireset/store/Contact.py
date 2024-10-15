from dataclasses import dataclass
from datetime import date, datetime
import typing as T
from uuid import UUID, uuid4

from parse import parse


@dataclass
class Adresse:
    id: int = -1
    boite_postale: str = ""
    adresse_etendue: str = ""
    rue: str = ""
    ville: str = ""
    region: str = ""
    code_postal: str = ""
    pays: str = ""
    type: str = ""
    prefered: bool = False

    def __eq__(self, value: "Adresse") -> bool:
        res = (
            self.id == value.id
            and self.boite_postale.replace(";", ",").strip()
            == value.boite_postale.replace(";", ",").strip()
            and self.adresse_etendue.replace(";", ",").strip()
            == value.adresse_etendue.replace(";", ",").strip()
            and self.rue.replace(";", ",").strip() == self.rue.replace(";", ",").strip()
            and self.ville.replace(";", ",").strip() == self.ville.replace(";", ",").strip()
            and self.region.replace(";", ",").strip() == self.region.replace(";", ",").strip()
            and self.code_postal.replace(";", ",").strip()
            == self.code_postal.replace(";", ",").strip()
            and self.pays.replace(";", ",").strip() == self.pays.replace(";", ",").strip()
            and self.type.replace(";", ",").strip() == self.type.replace(";", ",").strip()
            and self.prefered == self.prefered
        )
        return res

    @classmethod
    def getFormat(cls) -> str:
        fmt = "SOURCE:adr:{aid}\nitem{nb_item}.{pref_str}:{elems}\nitem{nb_item}.{type}"
        return fmt

    @classmethod
    def fromVcard(cls, data: bytes) -> "Adresse":
        s = data.decode(encoding="utf-8").strip()
        res = parse(cls.getFormat(), s)

        boite_postale, adresse_etendue, rue, ville, region, code_postal, pays = res["elems"].split(
            ";"
        )
        ret = cls(
            id=int(res["aid"]),
            boite_postale=boite_postale,
            adresse_etendue=adresse_etendue,
            rue=rue,
            ville=ville,
            region=region,
            code_postal=code_postal,
            pays=pays,
            type=res["type"].split("X-ABLABEL:")[1],
            prefered=res["pref_str"] != "ADR",
        )
        return ret

    def toVcard(self, nb_item: int) -> bytes:
        if self.prefered:
            pref_str = "ADR;TYPE=pref"
        else:
            pref_str = "ADR"
        elems = ";".join(
            [
                self.boite_postale.replace(";", ","),
                self.adresse_etendue.replace(";", ","),
                self.rue.replace(";", ","),
                self.ville.replace(";", ","),
                self.region.replace(";", ","),
                self.code_postal.replace(";", ","),
                self.pays.replace(";", ","),
            ]
        )
        res = Adresse.getFormat().format(
            aid=self.id,
            nb_item=nb_item,
            pref_str=pref_str,
            elems=elems,
            type="X-ABLABEL:" + self.type,
        )
        return res.encode(encoding="utf-8") + b"\n"


@dataclass
class Email:
    id: int = -1
    email: str = ""
    type: str = ""
    prefered: bool = False

    def __eq__(self, value: "Adresse") -> bool:
        res = (
            self.id == value.id
            and self.email.strip() == value.email.strip()
            and self.type.strip() == value.type.strip()
            and self.prefered == self.prefered
        )
        return res

    @classmethod
    def getFormat(cls) -> str:
        fmt = "SOURCE:email:{mid}\nitem{nb_item}.EMAIL{pref_str}TYPE=INTERNET:{email}\nitem{nb_item}.{type}"
        return fmt

    @classmethod
    def fromVcard(cls, data: bytes) -> "Email":
        s = data.decode(encoding="utf-8").strip()
        res = parse(cls.getFormat(), s)

        ret = cls(
            id=int(res["mid"]),
            email=res["email"],
            type=res["type"].split("X-ABLABEL:")[1],
            prefered=res["pref_str"] != ";",
        )
        return ret

    def toVcard(self, nb_item: int) -> bytes:
        if self.prefered:
            pref_str = ";TYPE=pref;"
        else:
            pref_str = ";"
        res = Email.getFormat().format(
            mid=self.id,
            email=self.email,
            pref_str=pref_str,
            nb_item=nb_item,
            type="X-ABLABEL:" + self.type,
        )
        return res.encode(encoding="utf-8") + b"\n"


@dataclass
class Telephone:
    id: int = -1
    telephone: str = ""
    type: str = ""
    prefered: bool = False

    def __eq__(self, value: "Adresse") -> bool:
        res = (
            self.id == value.id
            and self.telephone.strip() == value.telephone.strip()
            and self.type.strip() == value.type.strip()
            and self.prefered == self.prefered
        )
        return res

    @classmethod
    def getFormat(cls) -> str:
        # SOURCE:tel:42
        # item4.TEL:0102030409
        # item4.X-ABLabel:Customphone
        # ==================================
        # SOURCE:tel:53
        # item4.TEL;type=pref:0102030409
        # item4.X-ABLabel:Customphone
        fmt = "SOURCE:tel:{tid}\nitem{nb_item}.{pref_str}:{telephone}\nitem{nb_item}.X-{type}"
        return fmt

    @classmethod
    def fromVcard(cls, data: bytes) -> "Telephone":
        res = parse(cls.getFormat(), data.decode(encoding="utf-8").strip())

        ret = cls(
            id=int(res["tid"]),
            telephone=res["telephone"],
            type=res["type"].split("ABLabel:")[1],
            prefered=res["pref_str"] != "TEL",
        )
        return ret

    def toVcard(self, nb_item: int) -> bytes:
        if self.prefered:
            pref_str = "TEL;TYPE=pref"
        else:
            pref_str = "TEL"
        res = Telephone.getFormat().format(
            tid=self.id,
            nb_item=nb_item,
            telephone=self.telephone,
            pref_str=pref_str,
            type="ABLabel:" + self.type,
        )
        return res.encode(encoding="utf-8") + b"\n"


@dataclass
class Contact:
    # https://github.com/cozy/cozy-vcard/blob/master/test/ios-full.vcf
    id: int
    organisation: str
    fonction: str
    nom: str
    prenom: str
    civilite: str
    website: str
    date_naissance: date
    nom_de_naissance: str
    linkedin_profil: str
    notes: str
    photo: bytes
    adresses: T.List[Adresse]
    emails: T.List[Email]
    telephones: T.List[Telephone]
    etag: UUID

    def __eq__(self, value: "Adresse") -> bool:
        res = (
            self.id == value.id
            and self.organisation.strip() == value.organisation.strip()
            and self.fonction.strip() == value.fonction.strip()
            and self.nom.strip() == value.nom.strip()
            and self.prenom.strip() == value.prenom.strip()
            and self.civilite.strip() == value.civilite.strip()
            and self.website.strip() == value.website.strip()
            and self.date_naissance == value.date_naissance
            and self.nom_de_naissance.strip() == value.nom_de_naissance.strip()
            and self.linkedin_profil.strip() == value.linkedin_profil.strip()
            and self.notes.strip() == value.notes.strip()
            and self.photo == value.photo
            and self.etag == value.etag
        )
        return res

    @classmethod
    def _pick_info(cls, raw: bytes, data: dict):
        if raw.startswith(b"SOURCE:id:"):
            data["id"] = int(raw[10:])
        elif raw.startswith(b"ORG:"):
            orga = raw[4:].decode(encoding="utf-8")
            orga = orga.strip()
            if orga.endswith(";"):
                orga = orga[:-1]
            data["organisation"] = orga
        elif raw.startswith(b"TITLE:"):
            func = raw[6:].decode(encoding="utf-8")
            func = func.strip()
            if func.endswith(";"):
                func = func[:-1]
            data["fonction"] = func
        elif raw.startswith(b"N:"):
            elem = raw[2:].decode(encoding="utf-8").split(";")
            nom, prenom, _, civilite = elem[:4]
            data["nom"] = nom
            data["prenom"] = prenom
            data["civilite"] = civilite
        elif b".URL:" in raw:
            idx = raw.index(b".URL:")
            website = raw[idx + 5 :].decode(encoding="utf-8")
            data["website"] = website
        elif raw.startswith(b"BDAY;VALUE=date:"):
            sdt = raw[16:].decode(encoding="utf-8")
            dt = date.fromtimestamp(datetime.strptime(sdt, "%Y-%m-%d").timestamp())
            data["date_naissance"] = dt
        elif b"X-SOCIALPROFILE;X-USER=" in raw and b";TYPE=linkedin:" in raw:
            # X-SOCIALPROFILE;X-USER={user};TYPE=linkedin:
            idx = raw.index(b";TYPE=linkedin:")
            linkedin = raw[idx + 15 :].decode(encoding="utf-8")
            data["linkedin_profil"] = linkedin
        elif raw.startswith(b"NOTE:"):
            notes = raw[5:].decode(encoding="utf-8")
            data["notes"] = notes
        elif raw.startswith(b"PHOTO:data:image/jpeg;base64,"):
            data["photo"] = raw[29:]
        elif raw.startswith(b"SOURCE:etag:"):
            data["etag"] = UUID(raw[12:].decode())

    @classmethod
    def fromVcard(cls, data: T.Iterable[bytes]) -> "Contact":
        assert len(data) == 1

        contact_data = dict(
            id=-1,
            organisation="",
            fonction="",
            nom="",
            prenom="",
            website="",
            date_naissance=datetime.now(),
            nom_de_naissance="",
            civilite="",
            linkedin_profil="",
            notes="",
            photo=b"",
            adresses=[],
            emails=[],
            telephones=[],
            etag=uuid4(),
        )
        elems = list(data[0].split(b"\n"))
        raw: bytes
        for raw in elems:
            cls._pick_info(raw, contact_data)

        ret = cls(**contact_data)

        for iraw in range(len(elems) - 3):
            raw = elems[iraw]
            if raw.startswith(b"SOURCE:adr:"):
                a = Adresse.fromVcard(b"\n".join(elems[iraw : iraw + 3]))
                ret.adresses.append(a)
            elif raw.startswith(b"SOURCE:email:"):
                m = Email.fromVcard(b"\n".join(elems[iraw : iraw + 3]))
                ret.emails.append(m)
            elif raw.startswith(b"SOURCE:tel:"):
                t = Telephone.fromVcard(b"\n".join(elems[iraw : iraw + 3]))
                ret.telephones.append(t)

        return ret

    def toVcard(self) -> bytes:
        res = b""

        res += b"BEGIN:VCARD\n"
        res += b"VERSION:3.0\n"
        res += f"SOURCE:id:{self.id}\n".encode(encoding="utf-8")
        res += f"SOURCE:etag:{self.etag}\n".encode(encoding="utf-8")
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
            res += adresse.toVcard(nb_item)
            nb_item += 1

        for telephone in self.telephones:
            res += telephone.toVcard(nb_item)
            nb_item += 1

        if len(self.website) > 0:
            res += f"item{nb_item}.URL:{self.website}\n".encode(encoding="utf-8")
            res += f"item{nb_item}.X-ABLABEL:_$!<HomePage>!$_\n".encode(encoding="utf-8")
            nb_item += 1

        res += f"item{nb_item}.X-ABLABEL:_$!<ProfilePage>!$_\n".encode(encoding="utf-8")
        nb_item += 1

        for email in self.emails:
            res += email.toVcard(nb_item)
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
    etag=uuid4(),
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
