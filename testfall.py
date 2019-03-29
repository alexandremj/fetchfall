
import json
import requests

API_LINK = 'https://api.scryfall.com/'
DEFAULT_SIZE = 'normal'

# implement image_type as optional parameter
def named(card_name):
    name = card_name.replace(' ', '+')
    url = API_LINK + '/cards/named?fuzzy=' + name
    response_dict = json.loads(fetch_request(url))
    img_url = response_dict[DEFAULT_SIZE]
    filename = card_name.replace(' ', '_').lower() + DEFAULT_SIZE +'.jpg'
    download(filename, img_url) 

def download(filename, img_url):
    r = requests.get(img_url)

    if(r.status_code != 200):
        print('Request error at download(filename, img_url)')
        exit()

    with open(filename, 'wb') as img:
        img.write(r.content)

def fetch_request(url):
    r = requests.get(url)
    print(r)

    if(r.status_code != 200):
        print('Card not found!')
        print('This could have several reasons, for instance more than one card having this same name fragment, or no cards fitting the provided name')
        print('Please try again')
        exit()

    return r.json()

def main():
    try:
        card_name = input('Please insert the card name: ')
    except EOFError:
        print('Something unexpected happened')
        exit()
    named(card_name)

if __name__ == "__main__":
    main()
