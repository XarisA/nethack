#!/usr/bin/env python

import argparse
from socket import *


# Usage python portscanner.py -a 192.168.100.100 -p 21,80

def showBanner(connSock, tgtPort):
    try:
        # Send data to target
        if (tgtPort == 80):
            connSock.send("Get HTTP/1.1 \r\n")
        else:
            connSock.send("\r\n")

        # Receive data from target
        results = connSock.recv(4096)
        # Print the banner
        print '[+] Banner:' + str(results)
    except:
        print '[+] Banner not available\n'


def connScan(tgtHost, tgtPort):
    try:
        # Create the socket object
        connSock = socket(AF_INET, SOCK_STREAM)
        # Try to connect ith the target
        connSock.connect((tgtHost, tgtPort))
        print '[+] %d tcp open' % tgtPort
        showBanner(connSock, tgtPort)
    except:
        # Print the failure results
        print '[+] %d tcp closed' % tgtPort
    finally:
        # Close the socket object
        connSock.close()


def portScan(tgtHost, tgtPorts):
    try:
        # Resolve name to an ip
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Error: Unknown Host"
        exit(0)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print "[+] --- Scan result for: " + tgtName[0] + " ---"
    except:
        print '[+] --- Scan result for: ' + tgtIP + " ---"

    setdefaulttimeout(10)

    # Call the connScan function for eachport
    for tgtPort in tgtPorts:
        connScan(tgtHost, int(tgtPort))


def main():
    # Parsing the command line arguments
    parser = argparse.ArgumentParser('Smart TCP Client Scanner')
    parser.add_argument("-a", "--address", type=str, help="The target IP address",required=True)
    parser.add_argument("-p", "--port", type=str, help="The port number to connect with",required=True)
    args = parser.parse_args()

    # Store them
    ipAddress = args.address
    portNumbers = args.port.split(',')

    # portScan function
    portScan(ipAddress, portNumbers)


if __name__ == "__main__":
    main()
