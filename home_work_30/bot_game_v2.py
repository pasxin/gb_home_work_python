import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CommandHandler

reply_keyboard = [['/game_start', '/help'],
                  ['/close']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5667237284:AAFD0Tjsu48rNgI2oJTUxGb2uY5PQqSrpls'

def echo(update, context):
    
    return  update.message.text

def ferst_step(update, context):
    import random
    ferst_men = 0
    second_men = 0
    while ferst_men == second_men:
        update.message.reply_text ('Бросаем кости')
        ferst_men = random.randint (0,6)
        update.message.reply_text ('Игрок номер один выкинул: '+ str(ferst_men))
        second_men = random.randint (0,6)
        update.message.reply_text ('Бот выкинул: ' + str(second_men))
        if ferst_men == second_men: update.message.reply_text ('Равный результат. Бросаем кости еще раз. ')
    if ferst_men > second_men: 
        update.message.reply_text ("Первым ходит: Игрок")
        resultat = 1
    else:
        update.message.reply_text ("Первым ходит: Бот")
        resultat = 2
    return resultat


# Ход игрока
def player (update, context):
    updater = Updater(TOKEN)
    step = -1
    while step > 28 or step <= 0: 

        update.message.reply_text ((update, context))
        if step > 28 or step <= 0:
            update.message.reply_text ("Введено не корректное колличество. Введите занова")
    return step 

#Бот типа умный (ну как придумал)
def bot_hard (update, context, candies, player_step):
    mad = [i for i in range (candies+player_step-29,candies+player_step) if i%29==0]
    step = candies-int(mad [0])
    if step > 28 or step <= 0: step = 1
    update.message.reply_text ('Бот забирает ' + str(step) + ' конфет')
    return step

# Игра
def game_start (update, context,candies = 100):
    close_keyboard (update, context)
    step = ferst_step(update, context)
    player_step = 0
    while candies > 0:
        update.message.reply_text ('Осталось конфет на столе: '+ str(candies))
        if step == 1:
            update.message.reply_text ('Ход игрока. Сколько конфет заберете со стола?')
            player_step = player (update, context)
            candies -= player_step
            if candies <= 0:
                update.message.reply_text ("Победил игрок")
            step = 2
        elif step == 2:
            candies -= bot_hard (update, context,candies, player_step)   
            if candies <= 0:
                update.message.reply_text ("Победил бот")
            step = 1

def start(update, context):
    update.message.reply_text(
        "Я бот. Готовсыграть в игру.",
        reply_markup=markup
    )


def close_keyboard(update, context):
    update.message.reply_text(
        "Выключаем клавиатуру",
        reply_markup=ReplyKeyboardRemove()
    )

def help(update, context):
    update.message.reply_text(
        "Правила игры: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. \
    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все \
    конфеты оппонента достаются сделавшему последний ход")



def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(CommandHandler("game_start", game_start))
    dp.add_handler(game_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()