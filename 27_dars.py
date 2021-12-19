# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 20:16:31 2021

@author: User
"""
from transliterate import to_cyrillic, to_latin
import telebot
TOKEN = '687293161:AAEhFraX2FQYw8XaQlLJauRzhGXhH-dxGIg'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

print("Botni ishga tushirish uchun iltimos /start tugmasini bosing !")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    javob = "Assalomu alaykum, Niteuz_bot ga xush kelibsiz !"
    javob +="\nBot kiritilgan matnni (Krill -> Lotin) va (Lotin -> Krill) ga o'tkazadi !"
    javob += "\nMatn kiriting: "
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    
    # javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg) 
    # bot.reply_to(message, javob(msg))
    
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)

bot.infinity_polling()

# matn = input('Matnni kiriting - ')
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
    
    