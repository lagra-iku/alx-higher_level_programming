#!/usr/bin/python3
"""
takes your GitHub credentials (us
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print(f"Your user ID is: {user_data['id']}")
    else:
        print("Failed to fetch user data. Please check your credentials.")
