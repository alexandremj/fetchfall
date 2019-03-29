from testfall import named
import telegram

with open('token.txt', 'r') as f:
    TOKEN=f.read()

def main():
    bot = telegram.Bot(token=TOKEN)