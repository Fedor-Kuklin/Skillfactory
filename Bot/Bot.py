import telebot
from config import TOKEN, keys
from utils import ConvertException, CriptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def helps(message: telebot.types.Message):
    text = 'Команды:\n \
<имя валюты> <в какие валюты перевести> <количество переводимой валюты> - \
команда конвертации валюты>  \n \
< /values - команда показывает весь список доступных валют>\n\
< /help - справка по командам>\n\
Example:\n\
биткоин рубль - без количества\n\
биткоин рубль 2 - c количеством\n\
биткоин рубль доллар евро - перевести в несколько валют с количеством или без'

    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def operation(message: telebot.types.Message):

    messages = CriptoConverter(message.text)
    bot.send_message(message.chat.id, messages.command())


bot.polling(non_stop=True)