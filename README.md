# nethack

## *A suite for testing various networking tools build in python.*

## BruteForceFTP

### Brute Force Attack on FTP server *(Dictionary Attack)*

**Arguments**

- "-a", "--address", The target IP address
- "-d", "--dictionary", The path of the dictionary file
- "-s", "--singleuser", The username to attack (single user mode)
- "-u", "--userlist", The path of the file with the usernames to attack (do not use with -s)


*Examples:*
```
python BruteForceFTP.py -a 192.168.3.84 -d data/passwords.lst -u data/usernames.lst
python BruteForceFTP.py -a 192.168.3.84 -d data/passwords.lst -s ftpuser

```

## PortScanner

##### TODO

*I used python 2.7 for this project nevertheless most of the tools can probably be used with python 3.*

---
### This project moved to GitLab

https://gitlab.com/xaris/nethack
