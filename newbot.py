# -*- coding: utf-8 -*-
#!/usr/bin/env python 
token = '549317460:AAE-acIqR6RlSounvC7vp10Xkb8DUoYFwPQ'# - mybot
#    str('549317460:AAE-acIqR6RlSounvC7vp10Xkb8DUoYFwPQ')

#        03            05           1
# Караганда
Kcn03 = '4990'; Kcn05 = '7990'; Kcn1 = '12500'
Kkt03 = 15;   Kkt05 = 18;     Kkt1 = 0
# Алмаата
Acn03 = '4500'; Acn05 = '7500'; Acn1 = '11500'
Akt03 = 20;   Akt05 = 8;     Akt1 = 0



txt1 = txt0 = '''
Батарейки Пальчековые Заряд Энергие:
Вас приветствует магазин Energizer ! 
Работаем 24/7 360 дней
Уважаймые.жители Караганды и Алматы‼️
Компания Energizer изготавливает только качественные батарейки  созданные с применением современных технологий.
Благодаря этому она имеет ёмкость на 30-45 % больше, чем у источников питания предыдущего поколения.
Заряда батареи хватит вам на целый день а то и месяц.
Это делает её подходящей для использования в устройствах с высоким энергопотреблением

   💯💯Energizer💯💯
Это сервис каторый работает и радует вас‼️
Отзывы покупателей (нажмите 👉 /otzivi)
Оставить отзыв (нажмите 👉 /otziv)
Для покупки нажмите на свой город внизу:'''

txt2 = '''
Глава Профкома Vipole sonikbloody
Помощник Профкома Vipole sonikbiz2
Основной бот ТЕЛЕГРАМ  @Energzr_bot'''

txt3 = str('''
- сообщение о ненаходе не позднее 3х часов после получения адреса.
- картинку с геолокацией и фото, выданную ботом.
- фотографию на месте ненахода крупным планом.
- скриншот/фотографию чека
Контакты:
Vipole sonikbis2

Откупаясь на даном сервисе вы автоматически соглашаетесь с правилами данного сервиса Sonic Dash,
перезаклады не делаем все риски связанные с закладкой клиент берёт''')

txt4K = '''
Сейчас в наличии: 

➖➖➖➖Караганда➖➖➖➖

Батарея Energizer 
MAX AA-LR-0.33V за {0} тг. - {1} шт.
MAX AA BP-0.5V за {2} тг. - {3} шт.
MAX 9-9B-6LR-1V за {4} тг. - {5} шт.
'''.format(Kcn03, str(Kkt03), Kcn05, str(Kkt05), Kcn1, str(Kkt1))

txt4A = '''
➖➖➖➖Алмата➖➖➖➖

Батарея Energizer.
MAX AA-LR-0.33V за {0} тг. - {1} шт.
MAX AA BP-0.5V за {2} тг. - {3} шт.
MAX 9-9B-6LR-1V за {4} тг. - {5} шт.

Для покупки нажмите на свой город внизу:
'''.format(Acn03, str(Akt03), Acn05, str(Akt05), Acn1, str(Akt1))

txt4 = txt4K + txt4A

txt5 = '''
Вы выбрали "Караганда ". 
➖➖➖➖➖➖➖➖➖➖
Город: Караганда 
➖➖➖➖➖➖➖➖➖➖
Выберите товар:'''

txt6 = '''
Вы выбрали "Батарея Energizer". 
➖➖➖➖➖➖➖➖➖➖
Город: Караганда 
Товар: Батарея Energizer
➖➖➖➖➖➖➖➖➖➖
Выберите фасовку:'''


txt5a = '''
Вы выбрали "Алмата ". 
➖➖➖➖➖➖➖➖➖➖
Город: Алмата 
➖➖➖➖➖➖➖➖➖➖
Выберите товар:'''

txt6a = '''
Вы выбрали "Батарея Energizer". 
➖➖➖➖➖➖➖➖➖➖
Город: Алмата 
Товар: Батарея Energizer
➖➖➖➖➖➖➖➖➖➖
Выберите фасовку:'''

txt7_a03 = ('''
Вы выбрали MAX E91/AA BP-0.5V за {0}тг.
➖➖➖➖➖➖➖➖➖➖
Город: Караганда 
Товар: Батарея Energizer
Фасовка: ݂MAX E91/AA BP-0.5V за {1}тг.
➖➖➖➖➖➖➖➖➖➖
Выберите район:'''.format(Acn03))

txt7_a05 = ('''
Вы выбрали MAX E91/AA BP-0.5V за {0}тг.
➖➖➖➖➖➖➖➖➖➖
Город: Караганда 
Товар: Батарея Energizer
Фасовка: ݂MAX E91/AA BP-0.5V за {1}тг.
➖➖➖➖➖➖➖➖➖➖
Выберите район:'''.format(Acn05))

txt7_k05 = '''
Вы выбрали "݂MAX E91/AA BP-0.5V за 8000 тг.". 
➖➖➖➖➖➖➖➖➖➖
Город: Караганда 
Товар: Батарея Energizer
Фасовка: ݂MAX E91/AA BP-0.5V за 8000 тг.
➖➖➖➖➖➖➖➖➖➖
Выберите район:'''

txt =
Вы выбрали {} 
➖➖➖➖➖➖➖➖➖➖
Город: Караганда 
Товар: Батарея Energizer
Фасовка: ݂MAX AA-LR-0.33V за 4990 тг..
➖➖➖➖➖➖➖➖➖➖
Выберите район:'''


txt7_a03 = 
Вы выбрали "݂MAX AA-LR-0.33V за 4990 тг.". 
➖➖➖➖➖➖➖➖➖➖
Город: Караганда 
Товар: Батарея Energizer
Фасовка: ݂MAX AA-LR-0.33V за 4990 тг..
➖➖➖➖➖➖➖➖➖➖
Выберите район:'''


def vybor(grd, tov, fsv, rayon, qiwi):
    class grd
    if vybor(grd)==True:
        print('Вы выбрали "'+vybor.grd(grd)'". \n➖➖➖➖➖➖➖➖➖➖\n')
        print(vybor(i))"\n"

    grd={'Город': 'Караганда', 'Алмата'},  \nТовар: Батарея Energizer\nФасовка: ݂MAX AA-LR-0.33V за 4990 тг.\nРайон: Город\n➖➖➖➖➖➖➖➖➖➖\nВыберите способ оплаты:'

Вы выбрали "{vybor}". 
➖➖➖➖➖➖➖➖➖➖
Город: Караганда 
Товар: Батарея Energizer
Фасовка: ݂MAX AA-LR-0.33V за 4990 тг.
Район: Город
➖➖➖➖➖➖➖➖➖➖
Выберите способ оплаты:'''

txt9 = '''
Список поступивших платежей обновляется раз в пять минут, пожалуйста, подождите...

Переведите на QIWI в течение 24 часов
➖➖➖➖➖➖➖➖➖➖
Кошелек: +77083560420 
Сумма: 6000  тенге
Комментарий: 783 
➖➖➖➖➖➖➖➖➖➖
БЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ
'''


