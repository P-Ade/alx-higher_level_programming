#!/usr/bin/python3
"""A Python script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""


import urllib.request, sys

if __name__ == '__main__':
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        request = urllib.request.Request(url)
        print(dict(response.headers).get("X-Request-Id"))
