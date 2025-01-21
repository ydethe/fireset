from ldap3 import Server, Connection


server = Server("localhost:389")
conn = Connection(server, auto_bind=True)

print(server.info)
