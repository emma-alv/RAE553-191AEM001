from ftplib import FTP

ftp = ('ftp.lt.debian.org')
ftp.login()

data = ftp.retrlines('LIST')

print('Output of "LIST" on server {}'.format(ftp))
print(data)
