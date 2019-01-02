# nethack
---

A suite for testing various networking tools build in python.


Installation
---

```shell
# Download the file
$ wget https://github.com/XarisA/nethack/archive/master.zip -O nethack.zip

# Extract it and clean up
$ unzip nethack.zip -d nethack
$ mv nethack/nethack-master/* nethack && rm -rf nethack/nethack-master && rm nethack.zip
$ cd nethack

# Make it executable
$ chmod +x toolsname.py

# Run the program
$ ./toolsname.py
```

## BruteForceFTP
---

Dictionary Attack on FTP server

How to use:
---

```shell
python BruteForceFTP.py -h

usage: FTP Dictionary Attack [-h] -a ADDRESS -d DICTIONARY
                             (-s SINGLEUSER | -u USERLIST)

optional arguments:
  -h, --help            show this help message and exit
  -a ADDRESS, --address ADDRESS
                        The target IP address
  -d DICTIONARY, --dictionary DICTIONARY
                        The path of the dictionary file
  -s SINGLEUSER, --singleuser SINGLEUSER
                        The username to attack (single user mode)
  -u USERLIST, --userlist USERLIST
                        The path of the file with the usernames to attack (do
                        not use with -s)
```

```shell
# Make it executable
$ chmod +x BruteForceFTP.py

# Run the program
$ ./BruteForceFTP.py
```

Examples:
---

```
# Let the script call the interpreter (linux only)
$ ./BruteForceFTP.py -a 192.168.1.15 -d data/passwords.lst -u data/usernames.lst
$ ./python BruteForceFTP.py -a 192.168.1.15 -d data/passwords.lst -s ftpuser

# Calling the interpreter
$ python BruteForceFTP.py -a 10.0.14.87 -d data/passwords.lst -u data/usernames.lst
$ python BruteForceFTP.py -a 192.168.2.65 -d data/passwords.lst -s ftpuser
```


### TODO
---

- Clear CR characters
- Add support for python > 3


## PortScanner

`# TODO`
