#!/usr/bin/env python

import json
# aptitude install python-requests
import requests

url = "http://localhost:8080"
data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print("Status Code")
print(r.status_code)
print("URL")
print(r.url)
print("Encoding")
print(r.encoding)
print("Content")
print(r.content)
print("Json")
print(r.json())
