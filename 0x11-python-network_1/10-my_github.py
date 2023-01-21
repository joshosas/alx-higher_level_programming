#!/usr/bin/python3
"""
takes your Github credentials (username and password) and uses the Github API
to display your id
"""
if __name__ == '__main__':
    import requests
    import sys

    user = sys.argv[1]
    pawd = sys.argv[2]

    res = requests.get('https://api.github.com/user', auth=(user, pawd))

    data = response.json()
    print(data['id'])
