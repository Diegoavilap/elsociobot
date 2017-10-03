#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# importing Telegram libs and classes
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, os, json, random

token = os.environ['TELEGRAM_TOKEN']

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

"""
  Define a few command handlers. These usually take the two arguments bot and
  update. Error handlers also receive the raised TelegramError object in error.
"""

def knowledgeMA(t, who):
    # open the json file with custom messages
    with open('knowledge/data.json') as data_file:
        data = json.load(data_file)

    # check how many data on specific category
    # we set -1 because we need this number
    # to get data from array, and positions start
    # from 0, not 1
    count = len(data[t][who]) - 1
    # select a random number to later select a message
    r = random.randint(0, count)
    # return the random message from json
    return data[t][who][r]

# Let "El Socio" know who you want him to give a "madrazo"
def madrear(bot, update, args):
    try:
        # let's keep the name for the message
        real_name = args[0]
        # check which madrazo we need to send
        person = args[0]
        if person == 'oscar' | person = 'Oscar' | person = 'ozkar':
            person = 'oscar'
        elif person == 'reina' | person = 'Reina' | person = 'edwin':
            person = 'reina'
        else:
            person = 'general'

        # Request a madrazo for someone
        kn = knowledgeMA('madrazos', person)
        # Send random madrazo
        bot.send_message(chat_id=update.message.chat_id, text=kn.format(user_name=real_name))
    except (IndexError, ValueError):
        # When you set nothing with /madrear
        update.message.reply_text('Uso: /madrear <nombre del pirobo>')

# "El Socio" will give you a mapto his house
def micasa(bot, update):
    try:
        bot.send_message(chat_id=update.message.chat_id, text="Hogar de dioses")
        # Caney, of course ;)
        bot.send_location(chat_id=update.message.chat_id, latitude=3.29057260799024, longitude=-75.0142164941721)
    except (IndexError, ValueError):
        # In case something went wrong
        update.message.reply_text('Uso: /micasa')

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
    dp.add_handler(CommandHandler("micasa", micasa))

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
