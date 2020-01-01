# -*- coding: utf-8 -*-
from github import Github
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
import re

import config

github = Github(config.GITHUB_USER, config.GITHUB_PASS)
repo = github.get_repo(config.GITHUB_REPO_ISSUES)

logger = logging.getLogger("bot")


def welcome(bot, update):
    newMember = update.message.new_chat_members[0]
    bot.send_message(
        chat_id=update.message.chat_id, body=f"Bienvenido compañero {newMember}"
    )


def reply(bot, update):
    logger.info("Response sent")
    msg = update.message.text

    if re.search(r"[h|H]ola [d|D]aneel", msg):
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Hola compañero {}".format(update.message.from_user.first_name),
        )

    if re.search(r"[a|A]di[o|ó]s [d|D]aneel", msg):
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Adiós compañero {}".format(update.message.from_user.first_name),
        )


def proposeAwesomeList(bot, update):
    if re.search(r"\]\[", update.message.text):
        logger.info("Detected error in Markdown syntax")

        update.message.reply_markdown(
            f"He detectado un error en tu sintáxis. Recuerda que los enlaces en el lenguaje Markdown se escriben de la siguiente manera:\n`[texto a mostrar](enlace)`",
            quote=True,
        )

    else:
        logger.info("Issue created")
        resource = update.message.text.replace("/proponer ", "")
        resourceTitle = resource.split("]")[0].replace("[", "")
        user = update.message.from_user.username

        issue = f"{user} propone añadir el siguiente recurso:\n- {resource}"
        logger.info(issue)

        repo.create_issue(title=f"Recurso propuesto: {resourceTitle}", body=issue)

        update.message.reply_markdown(
            f"Recurso `{resourceTitle}` propuesto en una __issue__ en el repositorio de `makersGC/awesome-micropython`",
            quote=True,
        )


if __name__ == "__main__":
    updater = Updater(config.TOKEN)

    updater.dispatcher.add_handler(CommandHandler("proponer", proposeAwesomeList))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.status_update.new_chat_members, welcome)
    )

    updater.start_polling()
    updater.idle()
