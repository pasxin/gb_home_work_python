
from comands import *
def bd_catalog():
    print ('1 - Вывести в консоль Базу данных "Каталог"')
    print ('2 - Коректировать строку ')
    print ('3 - Добавить новую строку ')
    print ('4 - Удалить строку')
    menu = int(input ())
    if menu == 1:
        print_console ('catalog.csv','price')
    if menu == 2:
        text = read_file('catalog.csv')
        rename = int(input ('Укажите стрончу нобходимую скорректировать: '))
        print ("Данная строчка  " + str (text [rename]) + " будет скорректирована")
        print ("Что конкретно изменяем?")
        print ("1 - Продукт")
        print ("2 - Цена")
        print ("3 - Марка")
        menu_2  = int(input ())
        if menu_2 == 1:
            text [rename][0]= input ("Введите новое значение: ")
        if menu_2 ==2:
            text [rename][1]= input ("Введите новое значение: ")
        if menu_2 == 3:
            text [rename][2]= input ("Введите новое значение: ")
        print ('Новая строка будет выглядеть вот так:')
        print (text[rename])
        print ('1 - Подтвердить изменение')
        print ('2 - Отменить изменения')
        menu_3 = int(input ())
        if menu_3== 1:    
            re_file ('catalog.csv',text)
    if menu == 3:
        text = [input ("Введиет продукт: "),input ("Введиет цену: "),input ("Введиет марку: ")]
        add_text ('catalog.csv',text)
    if menu == 4:
        text = read_file('catalog.csv')
        rename = int(input ('Укажите стрончу нобходимую удалить: '))
        print ("Данная строчка  " + str (text [rename]) + " будет удалена")
        print ('1 - Подтвердить изменение')
        print ('2 - Отменить изменения')
        menu_3 = int(input ())
        if menu_3== 1:
            text.pop(rename)
            re_file ('catalog.csv',text)


    

    