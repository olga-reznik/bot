from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import datetime
import random
import os

def start(update=Update, context=CallbackContext):
    update.message.reply_text("Привет!")


def end(update=Update, context=CallbackContext):
    update.message.reply_text("Пока!")

def get_date(update=Update, context=CallbackContext):
    now= datetime.datetime.now()
    new_year = datetime.datetime(2023,1,1,0,0,0,0)
    delta = new_year - now
    answer_text = f"Сейчас {now.strftime('%d.%m.%Y %H:%M')}"
    answer_text += f"До нового года осталось {str(delta.days)} дней"
    update.message.reply_text(answer_text)


def number_analyze(word):
    analize_text = ""
    if word % 2 == 0:
        analize_text += "четное\n"
    else:
        analize_text += "не четное\n"

    if word > 0:
        analize_text += "положительное\n"
    elif word < 0:
        analize_text += "отрицательное\n"
    return analize_text


def echo(update=Update, context=CallbackContext):
    answer_text = "Вот что я думаю: "
    user_text = update.message.text

    #colors = ["желтый", "красный", "синий"]
    file= open("colors.csv", "r", encoding="UTF-8")
    file_text = file.read()
    colors = file_text.split(";")
    file.close()
    if user_text=="цвет":
        rand = random.randint(0,len(colors))
        answer_text += colors[rand]

    word_list = user_text.split(' ')
    numbers_count = 0

    for word in word_list:
        word.strip()
        if word.isdigit():
            answer_text += word + " - это число\n" + number_analyze(int(word))
            numbers_count += 1

        elif word.isalpha:
            pass

    if numbers_count == 0:
        answer_text += f"В твоем тексте нет чисел."
    elif numbers_count % 10 == 1:
        answer_text += f"В твоем тексте {numbers_count} число."
    elif 2 <= numbers_count % 10 < 5:
        answer_text += f"В твоем тексте {numbers_count} числа."
    elif numbers_count % 10 >= 5:
        answer_text += f"В твоем тексте {numbers_count} чисел."

    update.message.reply_text(answer_text)


def main():
    updater = Updater("5204544593:AAHkxMNw-zqFBOxNi4SJ2agnRRRKKrFMyTE")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("end", end))
    dispatcher.add_handler(CommandHandler("date", get_date))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()


main()
