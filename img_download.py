import requests

def download(card_name, url_dict):
    for key in url_dict:
        r = requests.get(url_dict[key])
        img = open('a.jpg', 'wb')
        img.write(r.content)
        img.close()

def main():
    download()

if __name__ == "__main__":
    main()
