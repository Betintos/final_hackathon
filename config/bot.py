import telebot
from django_filters import FilterSet
from settings import TELEGRAM_TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler


TOKEN = TELEGRAM_TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    message2 = bot.send_message(message.chat.id, 'Привет, чем могу помочь?')
    bot.register_next_step_handler(message2)

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(FilterSet.text & ~FilterSet.command, echo))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


bot.polling(none_stop=True)
