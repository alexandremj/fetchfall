from testfall import named
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import re

with open('token.txt', 'r') as f:
    TOKEN=f.read()

def named(update, context):
    print('Callback called')
    print(context.matches)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    regex = re.compile('\[\[([\w | \. | \s |,])*\]\]')
    named_handler = MessageHandler(Filters.regex(regex), 'named')
    dispatcher.add_handler(named_handler)
    updater.start_polling()

if __name__ == '__main__':
    main()