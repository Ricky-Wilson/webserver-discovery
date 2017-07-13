#!/usr/bin/env python

"""
Probe random web server and print out the title of their index page.

:param nhosts: The number of random IPs you want to probe.
"""

import os
import sys

# third party imports
import lxml.html


def get_title(url):
    """
    Extract the title from a web page..

    :param url: The URL of the page
    :returns: A string if title was found or None if somthing goes wrong
    """
    try:
        title = lxml.html.parse(url)
        return title.find(".//title").text
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception:
        return None

def shell(command):
    """
    Execute a shell command and return it's output.

    :param command: The command you want to execute
    :returns: A string representation of the commands output
    """
    return os.popen(command).read()

def scan(nhosts):
    """
    Scan for web servers.

    This function uses namp to find random systems
    that are running a service on port 80.
    We will assume that if the system is running a service
    on port 80 it's a web server and generate a URL for it.

    :param nhosts:  The number of random IPs you would like to probe
    :returns: A list if URLs
    """
    results = set(shell('./discover.sh {}'.format(nhosts)).split('\n'))
    if not results:
        print 'Nothing Found.'
        sys.exit(0)
    return ["http://{}".format(ip) for ip in results if ip]

def main():
    """
    This function puts everything together
    :returns: None
    """
    if not len(sys.argv) >= 2:
        print 'You forgot to tell me how many hosts to check'
        sys.exit(0)
    for url in scan(sys.argv[1]):
        title = get_title(url)
        if title:
            print title, url


if __name__ == '__main__':
    main()
