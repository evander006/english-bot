import random
import time

import telebot
from telebot import types

# Загружаем список books
f = open('books.txt', 'r', encoding='UTF-8')
books = f.read()
f.close()
# Загружаем список podcasts
f = open('podcasts.txt', 'r', encoding='UTF-8')
podcasts = f.read()
f.close()
# Загружаем список films
f = open('films.txt', 'r', encoding='UTF-8')
films = f.read()
f.close()
# Создаем бота
TOKEN = '5469680835:AAGR6yzKuu8MdBKSmx16spheHWeRay2mZTE'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(m, res=False):
    # Добавляем кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Книги')
    item2 = types.KeyboardButton('Подкасты')
    item3 = types.KeyboardButton('Фильмы')
    item4 = types.KeyboardButton('Давай поиграем!')
    item5 = types.KeyboardButton('Шпоргалки')
    markup.row(item1, item2, item3)
    markup.row(item4, item5)
    name = m.from_user.first_name
    lastName = m.from_user.last_name
    bot.send_message(m.chat.id, f"Hey, <u>{name} {lastName}</u>! 😁 \n \n"
                                "<b>Это бот Ева, E&E.</b> Расшифровывается English and Eva.\n \nЕсли ты жаждешь учить "
                                "английский 🔥, развиваться и быть успешнее других 👑, то тебе определённо нужна моя помощь. "
                                "\n \nЗдесь ты найдешь нужную тебе информацию и контент, который придётся по душе. Я "
                                "бот, который борется со стандартами и хочет, чтобы изучение языков приносило радость "
                                "и свет! 😘", parse_mode='html')
    time.sleep(2)
    bot.send_message(m.chat.id, 'Нажми: \n \n📖Книги, чтобы получить список лучших книг на английском\n \n🎧Подкасты, '
                                'чтобы слушать больше на английском\n \n📺Фильмы, если ты киноман и хочешь услышать речь '
                                'со своими любимыми актёрами', reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def user_message(message):
    words = ['word - мир', 'earth - земля', 'enough - достаточно', 'represent - представлять', 'sequence - последовательность', 'piece - кусок']
    if message.text.strip() == 'Книги':
        answer = books
        bot.send_message(message.chat.id, answer)
    elif message.text.strip() == 'Подкасты':
        answer = podcasts
        bot.send_message(message.chat.id, answer)
    elif message.text.strip() == 'Фильмы':
        answer = films
        bot.send_message(message.chat.id, answer)
    elif message.text.strip() == 'Давай поиграем!':
        bot.send_message(message.chat.id, 'Сейчас ты научишься новым словам!')
        bot.send_message(message.chat.id, random.choice(words))
    elif message.text.strip() == 'Шпоргалки':
        bot.send_photo(message.chat.id, photo=open('body.jpg', 'rb'))
        bot.send_photo(message.chat.id, photo=open('irregular.jpg', 'rb'))
        bot.send_photo(message.chat.id, photo=open('idioms.jpg', 'rb'))
        bot.send_photo(message.chat.id, photo=open('places.jpg', 'rb'))

        # Отсылаем юзеру сообщение в его чат

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    yes = types.InlineKeyboardButton('Да', callback_data='yes')
    keyboard.add(yes)
    no = types.InlineKeyboardButton('Нет', callback_data='no')
    keyboard.add(no)
    bot.send_message(message.chat.id, text='Хочешь получить больше?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Нажми: \n📖Книги, чтобы получить список лучших книг на английском\n🎧Подкасты, '
                                'чтобы слушать больше на английском\n📺Фильмы, если ты киноман и хочешь услышать речь '
                                'со своими любимыми актёрами')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Не упусти свою возможность! Будет много интересного.\nНажми ДА')

# Запускаем бота
bot.polling(none_stop=True, interval=0)
