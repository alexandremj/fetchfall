from testfall import named
from telegram.ext import Updater, MessageHandler, Filters
import re

with open('token.txt', 'r') as f:
    TOKEN=f.read()

def named(update, context):
    print(context.matches)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    pattern = re.compile('\[\[([\w | \. | \s |,])*\]\]')
    regex_handler = MessageHandler(Filters.regex(pattern), named)
    dispatcher.add_handler(regex_handler)
    print('start polling')
    updater.start_polling()

if __name__ == '__main__':
    main()