# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# Определяем чей первый  (бросаем кость)
def ferst_step(x):
    import random
    if x == 1: who = 'Игрок номер два '
    else: who = 'Бот '
    ferst_men = 0
    second_men = 0
    while ferst_men == second_men:
        print ('Бросаем кости')
        ferst_men = random.randint (0,6)
        print ('Игрок номер один выкинул: ', ferst_men)
        second_men = random.randint (0,6)
        print (who + 'выкинул: ', second_men)
        if ferst_men == second_men: print ('Равный результат. Бросаем кости еще раз. ')
    if ferst_men > second_men: 
        print ("Первым ходит: Игрок №1")
        resultat = 1
    else:
        print ("Первым ходит: " + who)
        resultat = 2
    return resultat
    
# Мини меню игры
def menu ():
    resultat = 0
    while resultat != 1 or 2 or 3:
        print ('Выбор режима игры: ')
        print ('1 - Игрок против игрока')
        print ('2 - Игрок против легкого бота')
        print ('3 - Игрок против сложного бота')
        resultat = int (input ('Выбрать режим игры: '))
        return resultat

# Ход игрока
def player (who):
    step = -1
    while step > 28 or step <= 0:
        step = int (input ('Колличество забираемых конфет игроком № ' + str(who) + ': '))
        if step > 28 or step <= 0:
            print ("Введено не корректное колличество. Введите занова")
    return step 

#Простой бот
def bot_easy ():
    import random
    step = random.randint (1,28)
    print ('Бот забирает ', str (step),' конфет')
    return step

#Бот типа умный (ну как придумал)
def bot_hard (candies, player_step):
    mad = [i for i in range (candies+player_step-29,candies+player_step) if i%29==0]
    step = candies-int(mad [0])
    if step > 28 or step == 0: step = 1
    print ('Бот забирает ' + str(step) + ' конфет')
    return step

# Игра
def play (menu, step,candies = 2021):
    player_step = 0
    while candies > 0:
        print ('Осталось конфет на столе: ', candies)
        if step == 1:
            player_step = player (1)
            candies -= player_step
            if candies <= 0:
                print ("Победил игрок № 1")
            step = 2
        elif step == 2 and menu == 1:        
            candies -= player (2)
            if candies <= 0:
                print ("Победил игрок № 2")
            step = 1
        elif step == 2 and menu == 2:
            candies -= bot_easy ()
            if candies <= 0:
                print ("Победил бот")
            step = 1
        elif step == 2 and menu == 3:
            candies -= bot_hard (candies, player_step)   
            if candies <= 0:
                print ("Победил бот")
            step = 1

result_menu = menu ()
result_ferst_step = ferst_step(result_menu)
play (result_menu,result_ferst_step,145)
