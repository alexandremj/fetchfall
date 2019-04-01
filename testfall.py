
import json
import requests

API_LINK = 'https://api.scryfall.com/'
DEFAULT_SIZE = 'normal'

def named(card_name, image_size):
    name = card_name.replace(' ', '+')
    img_link = (API_LINK + 'cards/named?fuzzy=' + name + '&format=image'
                + '&version=' + image_size)
    try:
        img = get_request(img_link)
    except ValueError:
        print('Request not successful')
        exit()

    filename = card_name.replace(' ', '_').lower() + '_' + image_size +'.jpg'
    with open(filename, 'wb') as file:
        file.write(img.content)
    return filename

def get_request(url):
    r = requests.get(url)

    if (r.status_code == 200):
        return r

    # API specification states too many requests can result in a temporary
    # or permanent IP ban. Since we don't want this, we exit to cooldown
    if (r.status_code == 429):
        panic('GET 429 Too Many Requests on testfall.py')
    
    raise ValueError(r.status_code)

    return r

""" 
    When something really bad happens a notification is sent to my personal
    Telegram account
    Should be commented out when bot implementation is finished
"""
def panic(reason):
#     requests.get('https://api.telegram.org/bot' 
#                  + TOKEN 
#                  + '/sendMessage?chat_id=171119330&text='
#                  + reason)"""
    print(reason)
    exit()

def main():
    try:
        card_name = input('Insert the card name: ')
    except EOFError:
        print('Please insert a valid card name!')
        exit()
    try:
        image_size = input('Insert the card size: ')
    except EOFError:
        image_size = DEFAULT_SIZE

    named(card_name, image_size)

if __name__ == "__main__":
    main()
