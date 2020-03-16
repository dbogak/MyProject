import datetime
import pymongo
import busers

from bson.objectid import ObjectId
from datetime import datetime
from busers import botusers


girls = []

#url = "mongodb+srv://dbogak:552026@cluster0-lm0wt.mongodb.net/test?retryWrites=true&w=majority"
url = ('mongodb+srv://Svet:552026@devky-yc6iv.gcp.mongodb.net/Devky?retryWrites=true&w=majority')
#url = '127.0.0.1:27017'



def ddb():
    col.insert_many(dbase)


devky=[]

def go_girls(country = "Казахстан", city = "Актау", n=5):
    
    client = pymongo.MongoClient(url)
    db = client[country]
    col = db[city]
    
    cursor = col.find({})

    for devky in cursor[:n]:
        #devky.append(document)
        yield devky

    


#go_girls(country, city)
#for girl in girls:
#    print(girl['name']+' - '+str(girl['phone']))
#    print('-----------------------------------------------------')

''' url = ('mongodb+srv://Svet:552026@devky-yc6iv.gcp.mongodb.net/Devky?retryWrites=true&w=majority')
    client = pymongo.MongoClient(url)
    db = client[country]
    col = db.city'''
    

# Веб фреймворк получает post_id из URL и передает его в виде строки
def get():
    # Преобразовываем из строки в ObjectId:
    for girl in girls:
        girl.get(name)
        print(girl['name'])

def usr_db(usr):
    
    usr_id = usr.id
    if usr_id not in botusers:
        # Запишем в Mongo нового пользователя
        client = pymongo.MongoClient(url)
        db = 'Devky'
        collection = db["Users"]
        col.insert_one({"usr_id": usr.id, "username": usr.username,
                        "first_name": usr.first_name, "last_name": usr.last_name, "language_code": usr.language_code, "date": datetime.now()})
        print(usr)

# Запишем в busers нового пользователя

        botusers.append(usr_id)

        with open('busers.py', 'w') as file:
            file.write('botusers = ' + str(botusers))

        print('!!!!!!!!!!!!+++++++++++++++++++++++++++++++!!!!!!!!!!!')
        print(usr)
        print('----------busers нового пользователя---------------------------------------------')




'''
   for i_users in botusers:
        with open('ausers.py','w') as file:
                file.write(i_users)'''