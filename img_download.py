import requests

def download(url):
    r = requests.get(url)
    img = open('a.jpg', 'wb')
    img.write(r.content)
    img.close()

def main():
    download()

if __name__ == "__main__":
    main()
