import telebot
from telebot import types

import const
import json
import tobase
import busers
import pymongo
url = ('mongodb+srv://Svet:552026@devky-yc6iv.gcp.mongodb.net/Devky?retryWrites=true&w=majority')


from datetime import datetime
from const import bot_token as token, data

country = 'Казахстан'
girls = []




# only used for console output now


def listener(messages):

    for m in messages:
        if m.content_type == 'text':

            print(str(datetime.now()) + " - [" + str(m.chat.id) +
                  "]: " + str(m.chat.first_name) + ": - " + m.text)
            

bot = telebot.TeleBot(token)





@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    


    user_markup.row("А можно всех посмотреть")
    user_markup.row("Заполнить анкету(девушкам)")

    answer = '''Приветствую тебя друг!!!
    Ты находишься в Боте приватных знакомств.
        Мои контакты - @jogav'''
    tobase.usr_db(usr = message.from_user)#Запишем в users нового пользователя
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)

    


@bot.message_handler(func=lambda message: message.text == "А можно всех посмотреть")
#bot.message_handler(content_types=['text'])
def handle_text_all(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        
    user_markup.row('Россия', 'Казахстан')
    user_markup.row('Украина', 'Узбекистан')
    user_markup.row("Заполнить анкету(девушкам)")
    answer = 'Для начала выберите страну'

    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)

@bot.message_handler(func=lambda message: message.text in data.keys())
#bot.message_handler(content_types=['text'])
def handle_text_cities(message):

    country = message.text
    print('----------------------------> coutry = ' + country)
    
    
    btn = data[country]
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row(btn[0], btn[1], btn[2], btn[3])
    user_markup.row(btn[4], btn[5], btn[6], btn[7])
    user_markup.row(btn[8], btn[9], btn[10], btn[11])
    user_markup.row('Вернуться в начало')
    
    answer = 'Так держать'
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    return country
     
    
@bot.message_handler(func=lambda message: message.text in data[country])
#bot.message_handler(content_types=['text'])
def handle_text_girls(message):
       
    city = message.text
    print('----------------------------> country+city = ' + country + city)
    answer = '----------------------------> country+city = ' + country + city
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    
    for i in tobase.go_girls(country, city):
        file_id=i['photo_id']
        answer=city+' - '+i['name']
        bot.send_photo(message.from_user.id, file_id)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)

        
         
     
    

@bot.message_handler(func=lambda message: message.text == 'Следующие')
#bot.message_handler(content_types=['text'])
def handle_text_five(message):
    n=+5
    go_five(n)
                   
    
    

@bot.message_handler(func=lambda message: message.text == 'Вернуться в начало')
#bot.message_handler(content_types=['text'])
def handle_text_start(message):
    commands = ['start']
    handle_start(message)

      


# default handler for every other text
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(message):
    # this is the standard reply to a normal message
    bot.send_message(message.chat.id, "I don't understand \"" +
                     message.text + "\"\nMaybe try the help page at /help")

bot.set_update_listener(listener)  # register listener


try:
    if __name__ == '__main__':
        bot.polling(none_stop=True)
except:
    Exception('ConnectTimeoutError')


'''
    if message.text == 'Вернуться в начало':
        handle_start(message=message)
        #message.text = '/start'
        answer = 'Возвращаемся'

    btn_anket = telebot.types.KeyboardButton(
        text='https://t.me/devky_bot?command=/start'

    user_markup=telebot.types.InlineKeyboardMarkup()
        btn_my_site=telebot.types.InlineKeyboardButton(
            text='Вернуться в начало', url='https://t.me/devky_bot?/start')
        user_markup.add(btn_my_site)


@bot.message_handler(commands=['switch'])
def switch(message):
    user_markup = telebot.types.InlineKeyboardMarkup()
    switch_button = telebot.types.InlineKeyboardButton(
        text='Try', switch_inline_query="Telegram")
    user_markup.add(switch_button)
    bot.send_message(message.chat.id, "Выбрать чат",
                     reply_markup=user_markup)



'''