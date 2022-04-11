import random

import telebot

token = "5214973826:AAEm9_nKiqS5nOcAz_fwmre-3ZP3rS1HU8Y"

bot = telebot.TeleBot(token)

HELP = """
/help - Список доступных команд
/print  - напечать все задачи на заданную дату
/todo - добавить задачу
/random - добавить на сегодня случайную задачу
"""
RANDOM_TASKS = ['Написать Гвидо письмо', 'Выучить Python', 'Записаться на спорт',
                'Посмотреть 4 сезон Рик и Морти']
tasks = {

}


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)  # add task in dict
    text = "Task " + task + " add on date " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands="random")
def random_add(message):
    date = "today"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)  # add task in dict
    text = "Task " + task + " add on date " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    i = 0
    if date in tasks:
        text = date.upper() + ":\n"
        for task in tasks[date]:
            i = i + 1
            text = text + f'{i}. ' + task + '\n'
    else:
        text = "On is date taks is none"
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
