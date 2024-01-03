#!/usr/bin/python3
"""
a python script that uses requests to get error codes
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if (r.status_code > 400):
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)