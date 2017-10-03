#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# importing Telegram libs and classes
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, os

token = os.environ['TELEGRAM_TOKEN']

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

"""
  Define a few command handlers. These usually take the two arguments bot and
  update. Error handlers also receive the raised TelegramError object in error.
"""
# Let "El Socio" know who you want him to give a "madrazo"
def madrear(bot, update, args):
    try:
        # return the name of the person
        person = args[0]
        # This is not working right now, need to check if is a valid string
        if not person:
            update.message.reply_text('Escriba bien maricon')
            return

        # Sending a madrazo
        madrazo = "%s %s" % ('Callese hpta', person)
        bot.send_message(chat_id=update.message.chat_id, text=madrazo)
    except (IndexError, ValueError):
        # When you set nothing with /madrear
        update.message.reply_text('Uso: /madrear <nombre del pirobo>')

# This is what you get when try to talk with El Socio in private.
def nonCommandAnsw(bot, update):
    update.message.reply_text("Abrase pues, o es que le quedé gustando.")

# for error logging
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("madrear", madrear, pass_args=True))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, nonCommandAnsw))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
