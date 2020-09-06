import telebot
from time import sleep
from telebot import types

print("Getting bot TOKEN...")
sleep(0.9)
bot = telebot.TeleBot("1397967815:AAFfMg9CBLH9R99UBXaOYkUrGujot5jCw2U", parse_mode=None)
print("Starting bot configuration")
sleep(0.3)
print("Starting bot...")
sleep(2.3)
print("Bot started! url : https://t.me/{0.username}".format(bot.get_me()))
print("To exit press ^C")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	print(message.text)
	#keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("😜Как дела?")
	item2 = types.KeyboardButton("😎🥳Крутой денёк сегодня?")
	item3 = types.KeyboardButton("😁Привет!")
	markup.add(item1, item2, item3)
	#messages
	wlc = open('stickers\welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, wlc)
	bot.send_message(message.chat.id, "Добро пожаловать, <b>{0.first_name}</b>!\nЯ новый бот в телеграме написанный на Python!\nЧтобы пообщаться со мной нажмите на одну из кнопок".format(message.from_user), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def messaging(message):
	print(message.text)
	if message.chat.type == "private":
		if message.text == "😜Как дела?":
			bot.send_message(message.chat.id, 'Настроение у меня как всегда шикарно!😉'.format(message.from_user), parse_mode='html')
		elif message.text == "😎🥳Крутой денёк сегодня?":
			bot.send_message(message.chat.id, '🤩Каждый день невероятно крутой!🤩', parse_mode='html')
		elif message.text == "😁Привет!":
			bot.send_message(message.chat.id, 'Привет <b>{0.first_name}</b>!😁'.format(message.from_user), parse_mode='html')
		elif message.text == "bot.activate_secret":
			win = open('stickers/win.webp', 'rb')
			bot.send_message(message.chat.id, 'Оу, оу!\n😱Ты активировал пасхалку!😱\n😱Ты активировал пасхалку!😱\n😱Ты активировал пасхалку!😱\nСкоро мой разработчик доделает эту пасхалку и ты возможно получишь исходный код бота или даже токен от бота!😱', parse_mode='html')
			bot.send_sticker(message.chat.id, win)
		else:
			bot.send_message(message.chat.id, '🤯Прости, но я не знаю что ответить😧', parse_mode='html')
bot.polling(none_stop=True, interval=0)

print()
print("Stoping bot...")
sleep(1.4)
print("Cleaning messages and logs...")
sleep(1.8)
print("Bot stopped sucessfuly!")