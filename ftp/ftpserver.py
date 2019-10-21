# To enable the FTP server we can use python FTP server library which provides a
# high-levelportable interface to easily write very efficient, scalable and
# asynchronous FTP server with Python https://github.com/giampaolo/pyftpdlib
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# DummyAuthorizar is a class handing authentications and permissions of the FTP server
authorizer = DummyAuthorizer()

# Add user to the virtual user table with the following permissions
# "e" = change directo, "l" = list files, "r" = retrieve file,
# "a" = append data to an existing file, "d" = delete file or directory
# "f" = rename file or directory, "m" = create directory
# "w" = store a file to the server, "M" = change file mode (CHMOD)
# "T" = update file last modified time
authorizer.add_user("user", "password", "/root/RAE553-Fall", perm="elradfmwMT")

# Add an anonymous user to the virtual user table. Read-only permissions "elr"
authorizer.add_anonymous("/root/RAE553-Fall")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
