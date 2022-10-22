from turtle import clear
from file_redacted import txt_add, txt_add_line
from file_redacted import txt_reader 
from import_new_contakt import import_new_contakt as contakt
from file_redacted import csv_add_line
from file_redacted import csv_add

def menu():
    print ('1 - добавить новый контакт')
    print ('2 - Вывод даданных в консоль из файла')
    menu = int(input())
    if menu == 1:
        text = contakt()
        txt_add(text)        
        txt_add_line(text)
        csv_add_line (text)
        csv_add (text)
    elif menu == 2:
        print ('1 - из txt разделитель - пробел')
        print ('2 - из txt разделитель - новая строка')
        print ('3 - из csv разделитель - тире')
        print ('4 - из csv разделитель - запятая')
        menu_2 = int(input (''))
        if menu_2 == 1: 
            print (txt_reader('file_for_HW_27_line.txt'))
        elif menu_2 == 2: 
            print (txt_reader('file_for_HW_27.txt'))
        elif menu_2 == 3: 
            print (txt_reader('file_for_HW_27_line.csv'))
        elif menu_2 == 4: 
            print (txt_reader('file_for_HW_27.csv'))
