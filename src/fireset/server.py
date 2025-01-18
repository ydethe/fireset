# https://github.com/twisted/ldaptor/issues/154

from ldaptor.protocols.ldap.ldapserver import LDAPServer

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import Engine

from twisted.internet.protocol import ServerFactory

from .database import DatabaseLDAPEntry

Base = declarative_base()


class LDAPServerFactory(ServerFactory):
    protocol = LDAPServer

    def __repr__(self):
        return f"LDAPServerFactory '{self.db_engine.url}'"

    def __init__(self, db_engine: Engine):
        self.db_engine = db_engine
        self.tree = None
        self.reload_tree()

    def reload_tree(self):
        """
        Building LDAP tree.
        Call this method if you need to reload data from the database.
        """
        com_tree = DatabaseLDAPEntry("dc=com")
        example_tree = com_tree.addChild("dc=example", {})
        users_tree = example_tree.addChild("ou=users", {})

        db_session = Session(self.db_engine)

        for employee in db_session.query(Employee):
            users_tree.addChild(
                "uid={}".format(employee.uid),
                {
                    "uid": [employee.uid],
                    "givenName": [employee.first_name],
                    "sn": [employee.last_name],
                    "email": [employee.email],
                },
            )
            print(f"   User {employee.uid} added")

        db_session.close()

        self.tree = com_tree

        print("Directory initiated with mock data")


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    uid = Column(String(255), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)


def create_db():
    """Creating a database with a table of employees and a couple of rows"""
    db_engine = create_engine("sqlite://")
    Base.metadata.bind = db_engine
    Employee.__table__.create(bind=db_engine)

    db_session = Session(db_engine)

    employee1 = Employee()
    employee1.uid = "f.example"
    employee1.first_name = "First"
    employee1.last_name = "Example"
    employee1.email = "first@example.com"
    db_session.add(employee1)

    employee2 = Employee()
    employee2.uid = "s.example"
    employee2.first_name = "Second"
    employee2.last_name = "Example"
    employee2.email = "second@example.com"
    db_session.add(employee2)

    db_session.commit()
    db_session.close()

    return db_engine
