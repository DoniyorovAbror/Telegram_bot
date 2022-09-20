import telebot

from extensions import ConvertException, Covert
from config import TOKEN, tickers

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start', 'help'])
def handler_start(message):
    bot.send_message(message.chat.id, f'Добро пожаловать {message.chat.first_name}\nэтот бот конвертирует валюты\n'
                                      f'формат ввода - на <валюта> с <валюты> <1>')
    
@bot.message_handler(commands = ['values'])
def handler_values(message):
    tickers_str = "Допустимые валюты: \n"
    for i in tickers:
        tickers_str += i+"\n"
    bot.send_message(message.chat.id, f'{tickers_str}')

@bot.message_handler(content_types = ['text'])
def handler_text(message):
    splitted = message.text.lower().split()
    if len(splitted) == 3 and splitted[-1].isdigit():
        _to, _from, _amount = splitted
        try:
            converted = Covert.get_price(_to,_from,_amount)
        except ConvertException as e:
            bot.send_message(message.chat.id, str(e))
        else:
            bot.send_message(message.chat.id, f"{converted['result']:.3f}")
    else:
        bot.send_message(message.chat.id, "Запрос не правильный\nДля справки /help")

bot.polling(none_stop = True)


