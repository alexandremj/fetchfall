from testfall import named
from telegram.ext import Updater, MessageHandler, Filters
import re

TOKEN='bot.token'

def named(update, context):
    print(context.matches)
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
    updater.start_polling()

if __name__ == '__main__':
    main()
