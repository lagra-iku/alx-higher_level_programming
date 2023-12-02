#!/usr/bin/python3
"""
a python script that create search api using requests
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': q})
    if r.status_code == 200:
        json_data = r.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")
