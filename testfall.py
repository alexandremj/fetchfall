
import json
import requests

API_LINK = 'https://api.scryfall.com/'
DEFAULT_SIZE = 'normal'

def named(card_name, image_size):
    name = card_name.replace(' ', '+')
    img_link = (API_LINK + 'cards/named?fuzzy=' + name + '&format=image'
                + '&version=' + image_size)
    img = fetch_request(img_link)

    filename = card_name.replace(' ', '_').lower() + '_' + image_size +'.jpg'
    with open(filename, 'wb') as file:
        file.write(img.content) 

def fetch_request(url):
    r = requests.get(url)

    # API specification states too many requests can result in a temporary
    # or permanent IP ban. Since we don't want this, we exit to cooldown
    if(r.status_code == 429):
        print('GET 429 error')
        print('Stopping bot execution...')
        exit()

    if(r.status_code != 200):
        print('Card not found!')
        print('This could have several reasons, for instance more than one card having this same name fragment, or no cards fitting the provided name')
        print('Please try again')
        exit()

    return r

def main():
    try:
        card_name = input('Please insert the card name: ')
    except EOFError:
        print('Something unexpected happened')
        exit()
    named(card_name, 'small')

if __name__ == "__main__":
    main()
