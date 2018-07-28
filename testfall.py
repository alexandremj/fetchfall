
"""
Test code for a python Magic: the Gathering card fetcher using requests as the HTTP library of choice and Scryfall API
"""

import json
import requests
from img_download import download

API_link = 'https://api.scryfall.com/'

def named(card_name):
    name = card_name.replace(' ', '+')
    url = API_link + '/cards/named?fuzzy=' + name
    r = requests.get(url)

    if(r.status_code == 404):
        print('Card not found!')
        exit()

    cont = json.loads(r.content)
    large_uri = cont['image_uris']['large']
    return large_uri

def main():
    try:
        card_name = input('Please insert the card name: ')
    except EOFError:
        print('Something unexpected happened')
        exit()

    url = named(card_name)
    download(url)

if __name__ == "__main__":
    main()
