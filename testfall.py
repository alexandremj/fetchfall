
import json
import requests

API_LINK = 'https://api.scryfall.com/'
DEFAULT_SIZE = 'normal'

def search(regex):
    print('Search parameters: ' + regex)
    regex.replace(':',  '%3A')
    regex.replace('=', '%3D')
    response_dict = json.loads(fetch_request(API_LINK + '/search?q='))
    print(response_dict)

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
        print('Request error at download(filename, img_url')
        exit()

    img = open(filename, 'wb')
    img.write(r.content)
    img.close()

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
    mode = input('Insert usage mode: ')

    if mode == 'named':
        try:
            card_name = input('Please insert the card name: ')
        except EOFError:
            print('Something unexpected happened')
            exit()
        named(card_name)
    elif mode == 'search':
        regex = input('Search parameters (following scryfall guidelines): ')
        search(regex)

if __name__ == "__main__":
    main()
