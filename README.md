# RAE553-Fall
## FTP Protocol
### Prerequisites

* Aim of the work:
To get quantified with an operation of FTP protocol using Python library ftplib.

* Before to start we select a source which will be use as our FTP server, for this practical case we decide to use one of the mirrors on [Debian's web-site](https://www.debian.org/mirror/list) which is `ftp.lt.debian.org`

* To ensure that we are working in a safe way, that means in an environment that we can manipulate and don't have to worry if we broke it down, let's create a new environment in anaconda. A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated spaces for them that contain per-project dependencies for them.

> `$conda create -n 191AEM001_env`

---
### Python codification for FTP

* To establish the connection with the FTP server using python code is necessary import the library `ftplib`

* As the client side, we should define the FTP server to connect, as was mentioned before the server is `ftp.lt.debian.org`
