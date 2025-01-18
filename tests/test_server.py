import sys

from ldaptor.interfaces import IConnectedLDAPEntry

from twisted.internet import reactor
from twisted.python.components import registerAdapter
from twisted.python import log

from fireset.server import create_db, LDAPServerFactory


if __name__ == "__main__":
    engine = create_db()

    log.startLogging(sys.stdout)

    registerAdapter(lambda x: x.tree, LDAPServerFactory, IConnectedLDAPEntry)
    factory = LDAPServerFactory(engine)
    reactor.listenTCP(1346, factory)
    reactor.run()
