#!/usr/bin/python3
"""A Python script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""


import urllib.request
import sys

# Get the email from the command line argument
email = sys.argv[1]

# Set the URL
url = "http://www.example.com/send"

# Build the data for the POST request
data = {"email": email}

# Encode the data to be sent
data = urllib.parse.urlencode(data).encode("utf-8")

# Send the request and read the response
with urllib.request.urlopen(url, data) as response:
    response_data = response.read().decode("utf-8")
    print(response_data)
