#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
if __name__ == '__main__':
    from sys import argv
    import requests
    import json 

    url = 'http://0.0.0.0:5000/search_user'
    letter = argv[1] or ""
    data = {'q': letter}

    res = requests.post(url, json=data)

    try:
        json_response = json.loads(response.text)
        if json_response:
            for item in json_response:
                print(f"[{item['id']}] {item['name']}")
        else:
            print("No result")
    except json.decoder.JSONDecodeError:
        print("Not a valid JSON")
