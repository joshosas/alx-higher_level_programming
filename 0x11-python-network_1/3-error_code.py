#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL & displays the body of the response
"""
if __name__ == "__main__":
    import sys
    import urllib.request
    
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            html = res.read().decode("utf-8")
            print(html)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
