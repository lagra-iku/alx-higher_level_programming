#!/usr/bin/python3
"""
Retrieves 10 recent commit of owner
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner }/{repo }/commits"
    r = requests.get(url)
    if r.status_code == 200:
        response = r.json()
        if response:
            for i, item in enumerate(response[:10]):
                print(f"{item['sha']}: {item['commit']['author']['name']}")
        else:
            print("Unable to retrieve data")
    else:
        print("Not a valid JSON")
