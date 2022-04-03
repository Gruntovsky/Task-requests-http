import json
from pprint import pprint
import requests

heroes = ("https://superheroapi.com/api/2619421814940190/search/Captain_America",
          "https://superheroapi.com/api/2619421814940190/search/hulk",
          "https://superheroapi.com/api/2619421814940190/search/Thanos")

def test_request(heroes):
    url = heroes
    response = requests.get(url, timeout=5)
    p = response.json()
    result={}
    if 'powerstats' in p.get('results')[0]:
        result['name'] = p.get('results')[0].get('name')
        result['powerstats'] = p.get('results')[0].get('powerstats')
    return result

class Hero:
    def __init__(self,name,intelligence):
        self.name = name
        self.intelligence = intelligence
    def __str__(self):
            text = f'\nИмя:{self.name}\nИнтелект: {self.intelligence}'
            return text

cap = Hero(test_request(heroes[0])['name'],test_request(heroes[0]).get('powerstats')['intelligence'])
hulk = Hero(test_request(heroes[1])['name'],test_request(heroes[1]).get('powerstats')['intelligence'])
thanos = Hero(test_request(heroes[2])['name'],test_request(heroes[2]).get('powerstats')['intelligence'])

q=[int(cap.intelligence),int(hulk.intelligence),int(thanos.intelligence)]
personage=[cap,hulk,thanos]

for smart in personage:
    if int(smart.intelligence) == max(q):
        print('Cамый умный персонаж:',smart)