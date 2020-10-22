#!/usr/bin/env python3
import requests

BASE = "http://127.0.0.1:5000/"

# Test GET method on "http://127.0.0.1:5000/"
response = requests.get(BASE)
print(response.content)

# Test GET method on "http://127.0.0.1:5000/pokemon"
response = requests.get(BASE + "pokemon")
print(response.content)

# Test POST method on "http://127.0.0.1:5000/pokemon"
response = requests.post(BASE + "pokemon", data={'key': 'value'})
print(response.content)

# Test PUT method on "http://127.0.0.1:5000/pokemon"
response = requests.put(BASE + "pokemon", data={'key': 'value'})
print(response.content)
