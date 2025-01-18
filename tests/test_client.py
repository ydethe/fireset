from twisted.internet import reactor
from twisted.internet.endpoints import clientFromString, connectProtocol, TCP4ClientEndpoint
from twisted.internet.defer import Deferred
from ldaptor.protocols.ldap import distinguishedname
from ldaptor.protocols.ldap.ldapclient import LDAPClient


dn = distinguishedname.DistinguishedName("dc=example,dc=com")
print(dn.getText())

e: TCP4ClientEndpoint = clientFromString(reactor, "tcp:host=localhost:port=1346")
d: Deferred = connectProtocol(e, LDAPClient())
print(d)

# e.connect(LDAPClient)

# proto = d.result
# baseEntry = ldapsyntax.LDAPEntry(client=proto, dn=dn)
# d2 = baseEntry.search(filterText="(uid=*)")
# results = d2.result
# print(results)
