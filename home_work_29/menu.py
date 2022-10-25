from comands import *

def menu():
    file = 'file_for_HW_29.csv'
    print ('1 - добавить новый контакт')
    print ('2 - Вывод даданных в консоль из файла')
    print ('3 - Поиск по фамилии')
    print ('4 - Корректировка строки')
    menu = int(input())
    if menu == 1:
        text = import_new_contakt ()
        add_text (file,text)
    elif menu == 2:
        print_console (file,"Номер телефона")
    elif menu == 3:
        list = filter_name (file)
        if list[1] !=0:
            for row in list[0]:
                print (row)
    elif menu == 4:
        re = int(input ('Введите номер строки которую ходите скорректировать: '))
        list = read_file (file)
        print ('Данная строка будет скорректирована: ')
        print (list[re])
        print ('Что хотитие скорретировать?')
        print ('1 - Имя')
        print ('2 - Фамилию')
        print ('3 - Номер телефона')
        print ('4 - Примечание')
        menu_2 = int(input ("Введите новое знаение: "))
        if menu_2 == 1:
            list[re][0]= input ('')
        if menu_2 == 2:
            list[re][1]= input ('')
        if menu_2 == 3:
            list[re][2]= input ('')
        if menu_2 == 4:
            list[re][3]= input ('')
        print ('Новыя строка будет выглядеть: ')
        print (list [re])
        print ('Подтвердить изменения? ')
        print ('1 - Да')
        print ('2 - Нет')
        menu_2 = int(input())
        if menu_2 == 1: re_file (file,list)
            