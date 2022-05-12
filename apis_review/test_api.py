from requests import get
from json import dump
from os import environ

API_KEY = environ['GOOGLE_API']

url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

parameters = {
    'key': API_KEY,
    'query': 'restaurant',
    'location': '37.8210207,-122.248357',
    'radius': 5000
}

response = get(url, params=parameters)
# print(type(response))
# print()
# print(dir(response))
# print()

data = response.json()
# print(type(data))
# print()
# print(data)

with open('api_data.json', 'w') as fp:
    dump(data, fp)
