#!/usr/bin/python3
"""
a python script that takes arg and post and displays the response
and HTTP error
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
