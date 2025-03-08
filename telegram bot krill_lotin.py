from transliterate import to_latin, to_cyrillic

# print(to_latin('дастур'))

import telebot
TOKEN='7299890455:AAHniuxmX4kJSq4IpCnd--A8CY1FmfZUmSg'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, xush kelibsiz !"
    javob += "\nMatn kiriting : "
    bot.reply_to(message, javob)
    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.polling()

# matn=input(" Matn kiriting :")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn)) 