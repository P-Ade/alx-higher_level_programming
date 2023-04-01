#!/usr/bin/python3
"""A script that lists the 10 most recent commits on a given GitHub repository.
"""

import requests
import sys

repo_name = sys.argv[1]
owner_name = sys.argv[2]

url = 'https://api.github.com/repos/' + owner_name + '/' + repo_name + '/commits'

res = requests.get(url)

if res.status_code != 200:
    raise Exception('ERROR: API request unsuccessful.')

data = res.json()

for commit in data[:10]:
    print(f"{commit['sha']}: {commit['commit']['author']['name']}")
