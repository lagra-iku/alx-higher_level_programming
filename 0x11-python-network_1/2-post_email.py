#!/usr/bin/python3
"""
a python script that takes arg and post and displays the response
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    email = {"email" : sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
