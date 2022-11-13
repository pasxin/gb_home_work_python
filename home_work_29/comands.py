import csv
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler

bot_token = '5667237284:AAFD0Tjsu48rNgI2oJTUxGb2uY5PQqSrpls'    
bot = Bot(bot_token)

def filter_name (file):
    count = 0
    resultat = []
    second_name = input ('Фамилию необходимого контакта: ')
    with open(file, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';',)
        for row in reader:
            if row[1] == second_name:
                resultat.append (row)
                count+=1
    if count == 0: print ('В базе данных отсутствует человек с такой фамилией')
    return (resultat,count)

def filter_name_bot(file,second_name,context,update):
    count = 0
    list = []
    with open(file, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';',)
        for row in reader:
            if row[1] == second_name:
                list.append (row)
                count+=1
    if count !=0:
        for row in list:
            context.bot.send_message(update.effective_chat.id,f'{row[0]} {row[1]} {row[2]} {row[3]}')
    elif count == 0:
        context.bot.send_message(update.effective_chat.id,'Данного пользователя нет в базе данных') 

# чтение csv-файла
def read_file (file):
    resultat = []
    with open(file, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';',)
        for row in reader:
            resultat.append (row)
        return (resultat)

# чтение в словарь
def print_console (file,lable):    
    with open(file, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        expensive = sorted(reader, key=lambda x: int(x[lable]), reverse=True)
    for record in expensive:
        print(record)

def print_console_bot (file,lable,context,update):
    expensive = []
    with open(file, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        expensive = sorted(reader, key=lambda x: int(x[lable]), reverse=True)
    for record in expensive:
        context.bot.send_message(update.effective_chat.id,f'{record["Имя"]} {record["Фамилия"]} {record["Номер телефона"]} {record["Примечание"]}')
      
# запись в файл полностью
def re_file (file,text):    
    with open(file, 'w', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for row in text:
            writer.writerow(row)

# запись в файл (для перезаписи режим 'w')
def add_text (file,text):    
    with open(file, 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(text)


def import_new_contakt ():
    name = input ('Введите имя нового контакта: ')
    family = input ('Введите фамилию пользователя: ')
    nomber = input ('Введите номер телефона пользователя: ')
    coments = input ('Добавте коментарий: ')
    resultat = (name, family, nomber,coments)
    return resultat
   



