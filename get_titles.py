#!/usr/bin/env python

import os
import sys
import lxml.html
import socket


# Set connection timeout
#TIMEOUT = 30
#socket.setdefaulttimeout(TIMEOUT)


def get_title(url):
    try:
        t = lxml.html.parse(url)
        return t.find(".//title").text
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        return None

def shell(command):
    """Run a shell command
    return it's output as a string"""
    return os.popen(command).read()

def scan(nhosts):
    """Run an nmap scan of n hosts.
    This will return IPv4 addresses of hosts
    that are up and have a service running on
    port 80"""
    results = set(shell('./discover.sh {}'.format(nhosts)).split('\n'))
    if not results:
        print 'Nothing Found.'
        sys.exit(0)
    return ["http://{}".format(ip) for ip in results if ip]
       

if __name__ == '__main__':        
    for url in scan(10000):
        title = get_title(url)
        if title:
            print title, url


