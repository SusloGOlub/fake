from telebot import TeleBot
import telebot


print("Bot has been started")

types = telebot.types
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message)

	keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	order = types.KeyboardButton(text='💵Сделать заказ💵')
	quality = types.KeyboardButton(text='🔥Качество🔥')
	delivery = types.KeyboardButton(text='🚚Получение и оплата💴')
	ahtung = types.KeyboardButton(text='🔴ВАЖНО🔴')
	rybl = types.KeyboardButton(text='🇷🇺Рубли🇷🇺')
	grivnu = types.KeyboardButton(text='🇺🇦Гривны🇺🇦')
	dollar = types.KeyboardButton(text='🇱🇷Доллары🇱🇷')

	buttons_to_add = [order, grivnu, delivery, rybl, quality, dollar, ahtung]


	keyboard.add(*buttons_to_add)
	bot.send_message(message.chat.id, 'Привет, ты попал к боту по продаже фальша😊💵',  reply_markup=keyboard, parse_mode='HTML')
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == '💵сделать заказ💵':
        bot.send_message(message.chat.id, 'По поводу заказов➡️ @falshivue_dengu')
    elif message.text.lower() == '🔥качество🔥':
    	bot.send_photo(message.chat.id, ('https://i.ibb.co/KXFc1WY/photo-2020-02-22-19-41-23.jpg'), 'Качество 1в1 с оригиналом отличить может только эксперт.\n\n Заказать @falshivue_dengu\n\n Наши банкноты принимают в терминалах - EasyPay, IBOX с полной проходимостью!')
    elif message.text.lower() == '🚚получение и оплата💴':
    	bot.send_message(message.chat.id, 'Кладом или отправка почтой. Безопасней всего кладом.\n Оплата: BTC\n\n ⬇️BTC адресс уточняйте у опператора⬇️\n @falshivue_dengu')
    elif message.text.lower() == '🇷🇺рубли🇷🇺':
    	bot.send_photo(message.chat.id, ('https://i.ibb.co/GpVxYb3/rybl123.jpg'), 'Номинал 1000-2000-5000:\n\n 5,000 фальши - 1,500 RUB\n 10,000 фальши - 3,000 RUB\n 15,000 фальши - 4,500 RUB\n 20,000 фальши - 6,000 RUB\n 30,000 фальши - 8,000 RUB')
    elif message.text.lower() == '🇺🇦гривны🇺🇦':
        bot.send_photo(message.chat.id, ('https://i.ibb.co/VjNjZ11/photo-2020-02-22-11-57-04.jpg'), 'Номинал 100, 200, 500, 1000:\n\n 2000 фальши - 500 UAH\n 5,000 фальши - 1,000 UAH\n 12,000 фальши - 2,000 UAH\n 20,000 фальши - 3,000 UAH\n 30,000 фальши - 4,000 UAH')
    elif message.text.lower() == '🇱🇷доллары🇱🇷':
        bot.send_photo(message.chat.id, ('https://i.ibb.co/fQMWnqf/4c37e7bb78d40486fc408fa0d7d392a2.jpg'), 'Номинал 10, 20, 50, 100:\n\n 50 фальши - 20 USD \n 100 фальши - 30 USD\n 150 фальши - 50 USD\n 350 фальши - 100 USD\n 500 фальши - 150 USD')
    elif message.text.lower() == '🔴важно🔴':
        bot.send_message(message.chat.id, '🔴ВАЖНО🔴\n\n 🏴 НА РЯДУ С ЧАСТО ЗАДАВАЕМЫМИ ВОПРОСАМИ.\n\n 🏴 ДЕРЖИТЕ ИНСТРУКЦИЮ ПО БЕЗОПАСНОМУ И УСПЕШНОМУ ОТМЫВАНИЮ ФАЛЬШИ.\n\n 🏴 И О ТОМ КАК НЕ БОЯТСЯ ПОСЛЕДСТВИЙ.\n\n 🏴 1) ВЫ ЖЕ ПРИОБРЕТАЕТЕ ИСКЛЮЧИТЕЛЬНО В «БЛАГИХ» ЦЕЛЯХ.\n\n 🏴 А ИМЕННО РАЗЫГРАТЬ ДРУЗЕЙ НА КОРПОРАТИВЕ.\n\n 🏴 ИЛИ ДЛЯ НАСТОЛЬНЫХ ИГОР ВАЛЮТУ  ПОКУПАЕТЕ,В КОНЦЕ КОНЦОВ У ВАС СЪЁМКА КЛИПА.\n\n ИЛИ КАКОЙ ТО СЦЕНКИ ДЛЯ СТОРИСА В ИНСТАГРАМ,И ЧТОБЫ НЕ ГРОБИТЬ РЕАЛЬНЫЕ ДЕНЬГИ ,ВЫ ИСПОЛЬЗУЕТЕ «РЕАЛИСТИЧНЫЕ НЕ НАСТОЯЩИЕ»\n\n 🏴 2) ОТМЫВ.\n\n САМЫЙ БЕЗОПАСНЫЙ СПОСОБ ЭТО ТЕРМИНАЛЫ : IBOX,CITY 24\n\n ,И ТД.\n\n ТЕРМИНАЛ ПРИНИМАЕТ 100,200,500 ГРН БЕЗ ПРОБЛЕМ.\n\n НАШИ КУПЮРЫ ТЕРМИНАЛЫ ПРИНИМАЮТ БЕЗОТКАЗНО!\n\n 🏴 3) ОШИБКИ.\n\n НЕЛЬЗЯ НЕСТИ ЭТИ ДЕНЬГИ В БАНК И ЛОЖИТЬ НА ДЕПОЗИТ\n\n 🏴 НЕ НУЖНО ВКЛАДЫВАТЬ В 1 ТЕРМИНАЛ БОЛЬШЕ 2000 ГРН ЧТОБЫ НЕ ПРИВЛЕКАТЬ К СЕБЕ ВНИМАНИЕ.\n\n 🏴 4) «ЗАЧЕМ ПРОДАВАТЬ ФАЛЬШ ЕСЛИ МОЖНО ОТМЫВАТЬ САМОМУ?»\n\n 🏴 — ЕСЛИ СЛИВАТЬ В ОГРОМНЫХ КОЛИЧЕСТВАХ ТО НАМИ НЕПРЕМЕННО ЗАИНТЕРЕСУЮТСЯ.\n\n 🏴 НАМ НЕ НУЖНЫ ПРОБЛЕМЫ И МЫ ИХ НЕ СОЗДАЁМ.\n\n 🏴 ТИШЕ ЕДЕШЬ - ДАЛЬШЕ БУДЕШЬ.')    
    else:
        bot.send_message(message.chat.id, ' Непонятный для меня текст.\nЕсли есть вопрос пишите оператору ➡️ @falshivue_dengu')

bot.polling()