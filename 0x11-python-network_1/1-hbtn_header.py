#!/usr/bin/python3
"""
a python script that gets the X-Request-Id of a URL
"""
import sys
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        request_id = response.getheader('X-Request-Id')
        print(request_id)
