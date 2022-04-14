"""APIs and Requests Library Demo: Searching iTunes"""


import requests
import json


payload = {'term': 'They Might Be Giants',
           'media': 'music',
           'attribute': 'artistTerm',
           'entity': 'musicTrack'}

res = requests.get('https://itunes.apple.com/search',
                   params=payload)

print(res.url)

tmbg_songs = res.json()

# demo saving json file to look at keys:
# with open('tmbg.json', 'w') as f:
#     json.dump(tmbg_songs, f)

# num_results = tmbg_songs['resultCount']
# for i in range(num_results):
    # trackName = tmbg_songs['results'][i].get('trackName')
    # artistName = tmbg_songs['results'][i].get('artistName')
    # print(f'{trackName}: {artistName}')

for result in tmbg_songs['results']:
    trackName = result.get('trackName')
    artistName = result.get('artistName')
    print(f'{trackName}: {artistName}')

