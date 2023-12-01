#!/usr/bin/python3
"""
a python script that uses requests to get headers
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
