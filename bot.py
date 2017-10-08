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

# This search for everything except madrazos
def knowledgeG(t):
    # open the json file with custom messages
    with open('knowledge/data.json') as data_file:
        data = json.load(data_file)

    # check how many data on specific category
    # we set -1 because we need this number
    # to get data from array, and positions start
    # from 0, not 1
    count = len(data[t]) - 1
    # select a random number to later select a message
    r = random.randint(0, count)
    # return the random message from json
    return data[t][r]

# This search in json file for madrazos
def knowledgeM(t, who):
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
        if person == 'oscar' or person == 'Oscar' or person == 'ozkar':
            person = 'oscar'
        elif person == 'reina' or person == 'Reina' or person == 'edwin':
            person = 'reina'
        elif person == 'eddy' or person == 'Eddy':
            person = 'eddy'
        elif person == 'diego' or person == 'Diego' or person == 'Dieguito' or person == 'dieguito':
            person = 'diego'
        elif person == 'juan david' or person == 'Juan David' or person == 'ojitos':
            person = 'juand'
        else:
            person = 'general'

        # Request a madrazo for someone
        kn = knowledgeM('madrazos', person)
        # Send random madrazo
        bot.send_message(chat_id=update.message.chat_id,
                         text=kn.format(user_name=real_name))
    except (IndexError, ValueError):
        # When you set nothing with /madrear
        update.message.reply_text('Uso: /madrear <nombre del pirobo>')

# "El Socio" will give you a map to his house
def mihouse(bot, update):
    try:
        bot.send_message(chat_id=update.message.chat_id, text="Hogar de dioses")
        # Caney, of course ;)
        bot.send_location(chat_id=update.message.chat_id,
                          latitude=3.29057260799024,
                          longitude=-75.0142164941721)
    except (IndexError, ValueError):
        # In case something went wrong
        update.message.reply_text('Uso: /micasa')

# "El socio" will give you a photo or gif about The finger expression
def pistola(bot, update):
    try:
        # Request a 'The Finger expression image or gif' from json
        kn = knowledgeG('pistolas')

        if (kn == 'gatito'):
            # open the image with The Finger expression
            image = open('knowledge/pistola/images/gatito.jpg','rb')
            #send a image
            bot.sendPhoto(chat_id=update.message.chat_id,
                          photo=image)
        else:
            #send a gif
            bot.sendVideo(chat_id=update.message.chat_id,
                          video=kn)
    except(IndexError, ValueError):
        # In case something went wrong
        update.message.reply_text('Uso: /pistola')
# "El Socio" will give you a suggestion for a plan
def planear(bot, update):
    try:
        # Request a 'plan' from json
        kn = knowledgeG('planes')
        # Send random 'plan'
        bot.send_message(chat_id=update.message.chat_id,
                         text=kn)
    except (IndexError, ValueError):
        # When you get and error
        update.message.reply_text('Uso: /planear')

# "El Socio" will give you a suggestion for a 'excusa'
def excusas(bot, update):
    try:
        # Request a 'excusa' from json
        kn = knowledgeG('excusas')
        # Send random 'excusa'
        bot.send_message(chat_id=update.message.chat_id,
                         text=kn)
    except (IndexError, ValueError):
        # When you get and error /excusas
        update.message.reply_text('Uso: /excusas')

# Let "El Socio" know who you want him to give an "agradecimiento"
def agradecer(bot, update, args):
    try:
        # let's keep the name for the message
        real_name = args[0]

        # Request an 'agradecimiento' for someone
        kn = knowledgeG('agradecimientos')
        # Send random 'agradecimiento'
        bot.send_message(chat_id=update.message.chat_id,
                         text=kn.format(user_name=real_name))
    except (IndexError, ValueError):
        # When you set nothing with /agradecer
        update.message.reply_text('Uso: /agradecer <nombre del pirobo>')

def ayuda(bot, update):
    # A message when you don't know how to use it
    msg = "Hola {user_name}! Yo soy {bot_name}. \n\n"
    msg += "Esta joda es sencilla, los comandos son: \n\n"
    msg += "- Madrear a alguien: /madrear <nombre-del-pirobo> \n"
    msg += "- Saber la ubicacion de mi casa: /mihouse \n"
    msg += "- Le propongo un plan: /planear \n"
    msg += "- Agradecerle parcero: /agradecer <nombre-a-bendecir> \n"
    msg += "- Le roto una excusa: /excusas \n"
    msg += "- Explicarle de nuevo porque no entiende: /ayuda \n\n"
    msg += "Si le quedó claro papi? \n"

    # Send the help message
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg.format(
                         user_name=update.message.from_user.first_name,
                         bot_name=bot.name))

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
    dp.add_handler(CommandHandler("mihouse", mihouse))
    dp.add_handler(CommandHandler("planear", planear))
    dp.add_handler(CommandHandler("pistola", pistola))
    dp.add_handler(CommandHandler("agradecer", agradecer, pass_args=True))
    dp.add_handler(CommandHandler("excusas", excusas))
    dp.add_handler(CommandHandler("ayuda", ayuda))

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
