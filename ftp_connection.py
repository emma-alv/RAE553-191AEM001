from ftplib import FTP

link = 'ftp.lt.debian.org'
ftp = FTP(link)
ftp.login()

data = ftp.retrlines('LIST')

print('Output of "LIST" on server {}'.format(link))
