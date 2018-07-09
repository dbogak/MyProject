import telebot
import constants
from constants import token1
from datetime import datetime
from ausers import botusers

bot = telebot.TeleBot(constants.token1)
answer = 'Приветствую тебя друг!!!'
answer = globals

@bot.message_handler(commands=['start'])
def handle_start(message):
    answer = '''Приветствую тебя друг!!!
    Ты находишься в Административной панели бота автопродаж.
    Вот список доступных команд:
    /des - добавит описание твоего магазина. То, что пользователь
    увидит, нажав кнопку '/start'.
    /help - инструкции под кнопку 'помощь'
    /gorod - После ее ввода добавляется новый город и автоматически
    продолжается ввод данных по предлагаемым тобой товарам.
    /set - Настройка существующего бота'''

#Запишем в users нового пользователя
    
    if message.from_user.id not in botusers:
        botusers.append(message.from_user.id)
        print('!!!!!!!!!!!!++++++++++++++!!!!!!!!!!!')
        with open('ausers.py','w') as file:
            file.write('botusers='+str(botusers))
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    user_markup.row("Добавить нового бота", "Настройка существующего")
   
    user_markup.row("В главное меню", "Прайс", "Помощь")
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)

@bot.message_handler(commands=['help'])
def handle_text(message):
    answer = 'Настройки существующего'
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup) 

@bot.message_handler(commands=['set'])
def handle_text(message):
    answer = 'Помоги себе сам'
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup) 

@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Ты поц, гыгы"
    if message.text != "#":
        answer = str('b')
        bot.send_message(message.chat.id, answer)
    print("--------------------------------------------------------")
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}, message_id={4}) = {3}".format(
    message.from_user.first_name, message.from_user.last_name,
    str(message.from_user.id), message.text, message.message_id))
    print(botusers)

if __name__ == '__main__':
    bot.polling(none_stop=True)

'''import telebot
import constants
from constants import txt1, txt2, txt3, txt4, txt5k, txt6k, txt5a, txt6a, txt7_a03, txt7_a05, txt7_k03,\
                        txt7_k05, txt8_k03g, txt8_k05g, txt8_a05g, txt8_k05g, txt9, Kbat03, Kbat05, Kbat10, Kkt03, Kkt05, Kkt1,\
                        Abat03, Abat05
#Alm[*], uvse[*]

bot = telebot.TeleBot(constants.token)
file = globals
@bot.message_handler(commands=['start'])
def handle_start(message):
    

    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    user_markup.row("Караганда", "Алмата")
    user_markup.row("Контакты магазина", "Ненаход")
    user_markup.row("Инструкция по оставлению отзыва в боте")
    user_markup.row("В главное меню", "Прайс", "Помощь")
    bot.send_message(message.from_user.id, txt1, reply_markup=user_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    global answer
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)


    log(message, answer)
    bot.send_message(message.chat.id,answer)
    
@bot.message_handler(commands=['settings'])
def handle_text(message):
    answer = "Тут пусто)"
    log(message, answer)
    bot.send_message(message.chat.id,answer)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Ты поц, гыгы"
    if message.text == "#":
        answer = str('b')
        log(message, answer)
        bot.send_message(message.chat.id, answer)

    elif message.text == "e":
        answer = "Ты лол"
        log(message, answer)
        bot.send_message(message.chat.id,answer)
    else:
        log(message, answer)
        bot.send_message(message.chat.id,answer)


@bot.message_handler(commands=['start'])
def begin(message):
    for id in users_id:
        if id != message.from_user.id:
            users_id.append(message.from_user.id)
            print(users_id) '''

