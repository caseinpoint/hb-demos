"""APIs and Requests Library Demo: Searching iTunes"""


import requests
import json
from pprint import pprint


# res = requests.get('https://itunes.apple.com/search?term=honeydew')

# print(res)
# print(dir(res))

# search_results = res.json()
# print(search_results)


payload = {'term': 'They Might Be Giants',
           'media': 'music',
           'attribute': 'artistTerm',
           'entity': 'musicTrack'}

res = requests.get('https://itunes.apple.com/search',
                   params=payload)

print(res.url)

# print(res.text)

tmbg_songs = res.json()
# print(tmbg_songs)
# pprint(tmbg_songs)

# demo saving json file to look at keys:
with open('tmbg.json', 'w') as f:
    json.dump(tmbg_songs, f)

# for result in tmbg_songs['results']:
#     trackName = result.get('trackName')
#     artistName = result.get('artistName')
#     print(f'{trackName}: {artistName}')

# num_results = tmbg_songs['resultCount']
# for i in range(num_results):
    # trackName = tmbg_songs['results'][i].get('trackName')
    # artistName = tmbg_songs['results'][i].get('artistName')
    # print(f'{trackName}: {artistName}')

