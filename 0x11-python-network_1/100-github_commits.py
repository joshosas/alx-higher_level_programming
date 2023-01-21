#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    ownr = sys.argv[2]

    res = requests.get(f'https://api.github.com/repos/{ownr}/{repo}/commits')
    commits = res.json()

    for commit in commits[:10]:
        print(f'{commit["sha"]}: {commit["commit"]["author"]["name"]}')
