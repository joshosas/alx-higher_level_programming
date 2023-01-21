#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import requests
    res = requests.get('https://intranet.hbtn.io/status')
    text = res.text
    print("Body response:$")
    print(f"\t- content: {res.headers['content-type']}$")
    print(f"\t- content: {text}")

