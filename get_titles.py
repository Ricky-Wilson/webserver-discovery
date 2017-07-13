#!/usr/bin/env python

""" Probe random web server and print out the title of their index page. """

import os
import sys

import lxml.html


def get_title(url):
    '''Extract the title from a webpage.
    If anything goes wrong like the request
    times out or the page does not have a
    title get_title will return None'''
    try:
        title = lxml.html.parse(url)
        return title.find(".//title").text
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception:
        return None

def shell(command):
    """Run a shell command.
    return it's output as a string"""
    return os.popen(command).read()

def scan(nhosts):
    """Run an nmap scan of n hosts.
    This will return IPv4 addresses of hosts
    that are up and have a service running on
    port 80. Simply supply the number of hosts
    you would like to check."""
    results = set(shell('./discover.sh {}'.format(nhosts)).split('\n'))
    if not results:
        print 'Nothing Found.'
        sys.exit(0)
    return ["http://{}".format(ip) for ip in results if ip]

def main():
    """ Run the scan."""
    if len(sys.argv) < 2:
        print 'You forgot to tell me how many hosts to check'
        sys.exit(0)
    for url in scan(sys.argv[1]):
        title = get_title(url)
        if title:
            print title, url


if __name__ == '__main__':
    main()
