#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL & displays the body of the response
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    res = requests.get(argv[1])
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
