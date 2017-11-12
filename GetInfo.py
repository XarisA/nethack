import os
from socket import *
import dns.resolver

# TODO Implement a module that gets information about the host
# TODO Pass arguments from terminal
# TODO Make every function os independent

def reach_host(hostname,arguments='-c 1'):
    # Pinging the host
    print '[+] Pinging ' + hostname
    if os.system("ping " + arguments + ' '+ hostname) == 0:
        print "Host appears to be up "
    else:
        print "Host is down or does not reply to ping requests "


def nslookup(hostname, typ3='MX'):
    answers = dns.resolver.query(hostname, typ3)
    for rdata in answers:
        print 'Host', rdata.exchange, 'has preference', rdata.preference


def main():
    hostname = "dnspython.org"
    print '[+] Gatering information about host'
    reach_host(hostname)
    print "Mail server lookup "
    nslookup(hostname)


if __name__ == "__main__":
    main()
