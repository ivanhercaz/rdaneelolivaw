from github import Github
from telegram.ext import Updater, CommandHandler

import logging

import config

github = Github(config.GITHUB_USER, config.GITHUB_PASS)
repo = github.get_repo(config.GITHUB_REPO_ISSUES)

logger = logging.getLogger("bot")


def hello(bot, update):
    update.message.reply_text(
        'Hola compañero {}'.format(update.message.from_user.first_name))


def proposeAwesomeList(bot, update):
    logger.info("Issue created")
    resource = update.message.text.replace("/proponer ", "")
    resourceTitle = resource.split("]")[0].replace("[", "")
    user = update.message.from_user.username

    labels = [repo.get_label("enhancement"),
              repo.get_label("telegram")]
    issue = f"{user} propone añadir el siguiente recurso:\n- {resource}"
    print(issue)

    repo.create_issue(
        title=f"Recurso propuesto: {resourceTitle}",
        body=issue,
        labels=labels
    )

    update.message.reply_markdown(
        f'Recurso `{resourceTitle}` propuesto en una en el repositorio de `makersGC/awesome-micropython`',
        quote=True)


updater = Updater(config.TOKEN)

updater.dispatcher.add_handler(CommandHandler('hola', hello))
updater.dispatcher.add_handler(CommandHandler('proponer', proposeAwesomeList))

updater.start_polling()
updater.idle()
