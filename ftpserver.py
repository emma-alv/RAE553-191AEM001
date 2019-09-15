from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "password", "/root/RAE553-Fall", perm="elradfmwMT")
authorizer.add_anonymous("/root/RAE553-Fall")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
