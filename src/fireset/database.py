from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import select

from . import settings


# https://docs.sqlalchemy.org/en/20/orm/extensions/automap.html
def list_vcards():
    Base = automap_base()

    engine = create_engine(settings.database_uri.unicode_string())

    # reflect the tables
    Base.prepare(autoload_with=engine)

    # mapped classes are now created with names by default
    # matching that of the table name.
    Contact = Base.classes.contact

    session = Session(engine)

    statement = select(Contact)

    # list of ``User`` objects
    for user_obj in session.scalars(statement).all():
        print(user_obj.nom)
