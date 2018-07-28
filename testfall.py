
"""
Test code for a python Magic: the Gathering card fetcher using requests as the HTTP library of choice and Scryfall API
"""

import json
import requests

API_link = 'https://api.scryfall.com/'

def named(card_name):
    name = card_name.replace(' ', '+')
    url = API_link + '/cards/named?fuzzy=' + name
    images = fetch_image_url(url)['image_uris']
    download(card_name, images)

"""
Card name is used only for naming of the files and may be
removed in future versions
Currently not supporting download of different sets
"""

def download(card_name, url_dict):
    for key in url_dict:
        r = requests.get(url_dict[key])
        img = open(card_name + '_' + key + '.jpg', 'wb')
        img.write(r.content)
        img.close()

"""
the uris are for:
small: 146x204 JPG
normal: 488x680 JPG
large: 672x936 JPG
png: 745x1040 PNG
art_crop: rectangular crop of the card's art
border_crop: most of the border cropped off
"""

def fetch_image_url(url):
    r = requests.get(url)

    if(r.status_code != 200):
        print('Card not found!')
        print('This could have several reasons, for instance more than one card having this same name fragment, or no cards fitting the provided name')
        print('Please try again')
        exit()

    return json.loads(r.content)

def main():
    try:
        card_name = input('Please insert the card name: ')
    except EOFError:
        print('Something unexpected happened')
        exit()

    named(card_name)

if __name__ == "__main__":
    main()
