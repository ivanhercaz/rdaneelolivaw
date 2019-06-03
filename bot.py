from telegram.ext import Updater, CommandHandler

import config


def hello(bot, update):
    update.message.reply_text(
        'Hola compañero {}'.format(update.message.from_user.first_name))


def proposeAwesomeList(bot, update):
    update.message.reply_text(
        'Recurso propuesto en una __issue__ en el repositorio de makersGC/awesome-micropython')


updater = Updater(config.TOKEN)

updater.dispatcher.add_handler(CommandHandler('hola', hello))
updater.dispatcher.add_handler(CommandHandler('proponer', proposeAwesomeList))

updater.start_polling()
updater.idle()
