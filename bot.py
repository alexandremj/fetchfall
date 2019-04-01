from testfall import named
from telegram.ext import Updater, MessageHandler, Filters
import re

with open('token.txt', 'r') as f:
    TOKEN=f.read()

def named(update, context):
    filename = testfall.named(context.matches)
    context.bot.sendPhoto(
                        chat_id=update.message.chat_id,
                        photo=open(filename),
                        reply_to_message_id=update.message.message_id
    )

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    regex = re.compile('\[\[([\w | \. | \s |,])*\]\]')
    regex_handler = MessageHandler(Filters.regex(regex), named)
    dispatcher.add_handler(regex_handler)
    print('start polling')
    updater.start_polling()

if __name__ == '__main__':
    main()