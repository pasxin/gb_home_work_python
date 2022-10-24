from comands import *

def menu():
    file = 'file_for_HW_29.csv'
    print ('1 - добавить новый контакт')
    print ('2 - Вывод даданных в консоль из файла')
    menu = int(input())
    if menu == 1:
        text = import_new_contakt ()
        add_text (file,text)
    elif menu == 2:
        print_console (file)

