#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
if __name__ == '__main__':
    from sys import argv
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    if argv > 2:
        letter = argv[1]
        q = {'q': letter}
    else:
        q = ""

    res = requests.post(url, json=q)

    try:
        json_response = json.loads(res.text)
        if json_response:
            for item in json_response:
                print(f"[{item['id']}] {item['name']}")
        else:
            print("No result")
    except json.decoder.JSONDecodeError:
        print("Not a valid JSON")
