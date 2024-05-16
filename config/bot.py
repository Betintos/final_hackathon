from .settings import TELEGRAM_TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = TELEGRAM_TOKEN

def start(update, context):
    update.message.reply_text('Привет, чем могу помочь?')

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


