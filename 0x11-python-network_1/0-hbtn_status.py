#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen('https://intranet.hbtn.io/status') as req:
        html = req.read()
        print('Body response:$')
        print("\t- type: {}$".format(html.info().get_content_type()))
        print("\t- content: {}$".format(html))
        print("\t- utf8 content: {}$".format(html.decode('utf-8')))

