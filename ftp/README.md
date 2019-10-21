# RAE553-Fall
## FTP Protocol
### Prerequisites

* Aim of the work:
To get quantified with an operation of FTP protocol using Python library ftplib.

* Before to start we select a source which will be use as our FTP server, for this practical case we decide to use one of the mirrors on [Debian's web-site](https://www.debian.org/mirror/list) which is `ftp.lt.debian.org`

* To ensure that we are working in a safe way, that means in an environment that we can manipulate and don't have to worry if we broke it down, let's create a new environment in anaconda. A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated spaces for them that contain per-project dependencies for them.

`$ conda create -n 191AEM001_env`

---
### Login to the FTP server

* To establish the connection with the FTP server using python code is necessary import the library `ftplib`

`>>> from ftplib import FTP`

* As the client side, we should define the FTP server to connect, as was mentioned before the server is `ftp.lt.debian.org`

```
>>> link = 'ftp.lt.debian.org'
>>> ftp = FTP(link)
>>> ftp.login()
```

* If the login is successful into the FTP server we will see a success message
`'230 Login successful.'`

---
### Workaround FTP

* Once we are connect to the FTP server we can test a couple commands.

* The first command will show us a list of current files and directories in the root directory where we are connected

`>>> data = ftp.retrlines('LIST')`

**Output**
```
drwxr-xr-x  198 ftp      ftp          8192 Sep 10 05:53 apache
drwxr-xr-x    9 ftp      ftp          4096 Sep 10 17:15 debian
drwxr-xr-x    5 ftp      ftp           102 Sep 10 17:12 debian-backports
drwxr-xr-x    5 ftp      ftp           127 Sep 08 16:43 debian-cd
drwxr-xr-x    7 ftp      ftp           142 Sep 10 17:12 debian-security
-rw-r--r--    1 ftp      ftp           571 Sep 10 16:44 debian-sources.list
-rw-r--r--    1 ftp      ftp           566 Apr 16  2014 ftp-sources.list
drwxr-xr-x    4 ftp      ftp           127 Sep 10 17:12 raspbian
drwxr-xr-x   12 ftp      ftp          4096 Sep 10 14:14 releases
drwxr-xr-x    7 ftp      ftp          4096 Sep 10 17:17 ubuntu
-rw-r--r--    1 ftp      ftp           862 Sep 10 16:44 ubuntu-sources.list
```

* Also we can change the directory where we are working

`>>> ftp.cwd('debian')`

**Output**
`'250 Directory succesfully changed.'`

---
### Downloading files from FTP

* As the protocol mentioned (File Transfer Protocol), the main purpose of it is transfer file between server and client. So, we will download one of the files from our FTP server.

* First, we should make sure that our connection is established. [Login to the FTP server](https://github.com/emma-alv/RAE553-Fall#login-to-the-ftp-server)

* Before download the file we should defined the path and file name where this file is going to be downloaded.

`>>> out = '/home/user/README.html'`

* With the function `open()` we will read the file from the FTP and save it in the path defined before.

```
>>> with open(out, 'wb') as f:
...    ftp.retrbinary('RETR ' + 'README.html', f.write)
```

**Output**
`'226 Transfer complete.'`

---
# Upload files to FTP

* Our last task was to download a file, but what if we want to upload a file.

* To do this, we will edit the previous `README.html` file deleting all html tags and leaving it as simple txt file. To do so I used a simple awk script.

`$ awk '{gsub(/<[^>]*>/,""); print }' ./README.html > README2.txt`

* To upload the file we are going to use the function `open()` again.
```
>>> file_name='README2.txt'
>>> ftp.storbinary('STOR ' + file_name, open(file_name, rb))
```
---
# FTP server

* Besides to work as FTP client, also we can start our own FTP server using Python and the library `pyftpdlib`.

The python script to enable the ftp server you can follow in the file `ftpserver.py`
