from datetime import date
import typing as T

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import select

from . import settings
from .Contact import Contact, Telephone, Email, Adresse


# https://docs.sqlalchemy.org/en/20/orm/extensions/automap.html

Base = automap_base()

engine = create_engine(settings.database_uri.unicode_string())

# reflect the tables
Base.prepare(autoload_with=engine)

# mapped classes are now created with names by default
# matching that of the table name.
DbContact = Base.classes.contact
DbAdresse = Base.classes.adresse
DbOrganisation = Base.classes.organisation
DbEmail = Base.classes.email


def adresse_from_db(db_adr: DbAdresse, typ: str) -> Adresse:
    adr = Adresse(
        id=db_adr.id,
        boite_postale=db_adr.boite_postale,
        adresse_etendue=db_adr.adresse_etendue,
        rue=db_adr.rue,
        ville=db_adr.ville,
        region=db_adr.region,
        code_postal=db_adr.code_postal,
        pays=db_adr.pays,
        telephone=db_adr.telephone,
        type=typ,
        prefered=db_adr.prefered,
    )
    return adr


def contact_from_db(db_contact: DbContact) -> Contact:
    telephones = []
    for tel in db_contact.telephone_collection:
        telephones.append(
            Telephone(id=tel.id, telephone=tel.numero, type=tel.type, prefered=tel.prefered)
        )

    emails = []
    for mail in db_contact.email_collection:
        emails.append(Email(id=mail.id, email=mail.email, type=mail.type, prefered=mail.prefered))

    adresses = []
    for adr_map in db_contact.contact_adresse_collection:
        typ = adr_map.type
        db_adr = adr_map.adresse
        adresses.append(adresse_from_db(db_adr, typ))

    organisation = ""
    fonction = ""
    date_exp = date(1, 1, 1)
    org_adr = None
    for expe in db_contact.experience_collection:
        if expe.date_debut is None or expe.date_debut > date_exp:
            date_exp = expe.date_debut
            db_org = expe.organisation

            if len(db_org.organisation_adresse_collection) > 0:
                org_adr = adresse_from_db(
                    db_org.organisation_adresse_collection[0].adresse, "bureau"
                )

            organisation = db_org.nom
            fonction = expe.intitule

    if org_adr is not None:
        adresses.append(org_adr)

    if db_contact.photo is None:
        photo_data = b""
    else:
        photo_data = db_contact.photo

    if db_contact.notes is None:
        notes = ""
    else:
        notes = db_contact.notes

    if db_contact.date_naissance is None:
        date_naissance = date(1, 1, 1)
    else:
        date_naissance = db_contact.date_naissance

    if db_contact.website is None:
        website = ""
    else:
        website = db_contact.website

    if db_contact.linkedin_profile is None:
        linkedin_profile = ""
    else:
        linkedin_profile = db_contact.linkedin_profile

    contact = Contact(
        id=db_contact.id,
        organisation=organisation,
        fonction=fonction,
        nom=db_contact.nom,
        prenom=db_contact.prenom,
        website=website,
        date_naissance=date_naissance,
        nom_de_naissance=db_contact.nom_de_naissance,
        civilite=db_contact.civilite,
        linkedin_profil=linkedin_profile,
        notes=notes,
        photo=photo_data,
        adresses=adresses,
        emails=emails,
        telephones=telephones,
    )

    return contact


def list_db_vcards() -> T.Iterator[DbContact]:
    with Session(engine) as session:
        statement = select(DbContact)

        for db_contact in session.scalars(statement).all():
            yield db_contact


def get_contact_from_email(email: str) -> DbContact | None:
    with Session(engine) as session:
        statement = select(DbEmail).filter_by(email=email)
        email_objs = list(session.scalars(statement).all())
        if len(email_objs) == 0:
            return None

        contact = session.get(DbContact, email_objs[0].contact_id)

        return contact


def get_db_vcard(card_id: int) -> Contact | None:
    with Session(engine) as session:
        db_contact = session.get(DbContact, card_id)

        contact = contact_from_db(db_contact)

        return contact
