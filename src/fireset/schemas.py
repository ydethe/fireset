import typing as T
from datetime import datetime
import json
import enum

from pydantic import field_validator, BaseModel
import sqlalchemy as sa
from geoalchemy2 import WKBElement
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, UniqueConstraint, Column

from . import settings


# ==============================
# Database access
# ==============================
def get_engine():
    engine = create_engine(settings.database_uri, echo=False)
    SQLModel.metadata.create_all(engine)

    return engine


def get_db():
    engine = get_engine()

    with Session(engine) as session:
        yield session


def create_db_and_tables():
    engine = create_engine(settings.database_uri, echo=False)
    SQLModel.metadata.create_all(engine)


# ==============================
# Authentication objects
# ==============================
class FsUser(SQLModel):
    id: str | None = None
    login: str = None
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    avatar_url: str | None = None
    permissions: list[str] = None


class AdresseType(enum.Enum):
    domicile = "domicile"
    bureau = "bureau"
    secondaire = "secondaire"


class ExperienceType(enum.Enum):
    formation = "formation"
    professionnel = "professionnel"
    humanitaire = "humanitaire"


class OrganisationType(enum.Enum):
    Ecole = "Ecole"
    Entreprise = "Entreprise"
    Association = "Association"


class CiviliteType(enum.Enum):
    Monsieur = "Monsieur"
    Madame = "Madame"
    Mademoiselle = "Mademoiselle"
    Père = "Père"
    Frère = "Frère"
    Soeur = "Soeur"


# ==============================
# Contact objects
# ==============================
class ContactBase(SQLModel):
    date_creation: datetime = Field(nullable=False)
    date_modification: datetime = Field(nullable=False)
    nom: str = Field(nullable=False)
    prenom: str = Field(nullable=False)
    particule: str = Field(nullable=True)
    civilite: CiviliteType = Field(
        sa_column=Column(sa.Enum(CiviliteType), default=None, nullable=True, index=False)
    )
    date_naissance: datetime = Field(nullable=True)
    nom_de_naissance: str = Field(nullable=True)
    profil_linkedin: str = Field(nullable=True)

    @field_validator("position", mode="before")
    def convert_geom_to_geojson(cls, v):
        if v is None:
            # Probably unnecessary if field is not nullable
            return None
        elif isinstance(v, WKBElement):
            # e.g. session.get results in a `WKBElement`
            v = sa.func.ST_AsGeoJSON(v)
        elif isinstance(v, sa.func.ST_AsGeoJSON):
            # e.g. session.exec(select(Aoi)).all() gives v as an instance of sa.func.ST_AsGeoJSON
            pass
        else:
            raise ValueError(f"Received unexpected type: {type(v)}")

        # Convert sa.func.ST_AsGeoJSON to json, which geojson-pydantic can then ingest
        engine = get_engine()
        with Session(engine) as session:
            return json.loads(session.scalar(v))


class Contact(ContactBase, table=True):
    idx: int | None = Field(default=None, primary_key=True)
    resultats: list["Resultat"] = Relationship(back_populates="contact", cascade_delete=True)


class ContactCreate(ContactBase):
    pass


class ContactPublic(ContactBase):
    id: int


class ContactUpdate(SQLModel):
    UAI: str | None = None
    nom: str | None = None
    adresse: str | None = None
    lieu_dit: str | None = None
    code_postal: str | None = None
    commune: str | None = None
    position: T.Any | None = None
    departement: str | None = None
    academie: str | None = None
    secteur: str | None = None
    ouverture: datetime | None = None
    nature: str | None = None


# ==============================
# Resultats objects
# ==============================
class ResultatBase(SQLModel):
    diplome: str = Field(nullable=False)
    annee: int = Field(nullable=False)
    presents: T.Optional[int] = Field(nullable=True)
    admis: T.Optional[int] = Field(nullable=True)
    mentions: T.Optional[int] = Field(nullable=True)
    etablissement_uai: str | None = Field(
        default=None, foreign_key="etablissement.UAI", ondelete="CASCADE"
    )


class Resultat(ResultatBase, table=True):
    __table_args__ = (UniqueConstraint("diplome", "annee", "etablissement_uai"),)

    idx: int | None = Field(default=None, primary_key=True)
    etablissement: Contact | None = Relationship(back_populates="resultats")


class ResultatPublic(ResultatBase):
    id: int


class ResultatCreate(ResultatBase):
    pass


class ResultatUpdate(SQLModel):
    diplome: str | None = None
    annee: int | None = None
    presents: int | None = None
    admis: int | None = None
    mentions: int | None = None
    etablissement_uai: str | None = None


class ResultatPublicAvecContact(ResultatPublic):
    etablissement: ContactPublic | None = None


class ContactPublicAvecResultats(ContactPublic):
    resultats: list[Resultat] = []


class QueryParameters(BaseModel):
    year: T.Optional[int] = None
    nature: T.Optional[T.List[str]] = None
    secteur: T.Optional[T.List[str]] = None
    stat_min: T.Optional[int] = None
