import telebot
from telebot import types
from time import sleep


bot = telebot.TeleBot("1251300918:AAHtD1W2Clz294i5r1haITmjH03NfYB7Mb0")
chat_for = "-1001394622167"
#@test_test_43_bot
#https://t.me/firechannel1
print("start")
@bot.message_handler(commands=['start'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button_yes = types.InlineKeyboardButton(text="Да, конечно✅", callback_data=f"yes{message.from_user.id}")
    callback_button_no = types.InlineKeyboardButton(text="Нет, не сейчас❎", callback_data="no")
    keyboard.add(callback_button_yes, callback_button_no)
    bot.send_message(message.chat.id, """Добро пожаловать {}!🙋‍♂️
Я являюсь ботом канала «🔥MAK-S ГОРЯЩАЯ РЕКЛАМА🔥».
Хотите ли Вы что то опубликировать на канале?""".format(message.from_user.first_name), reply_markup=keyboard)


@bot.message_handler(content_types = ['text'])
def reply_msg(message):
    if len(message.text) > 20:

        bot.forward_message(chat_for,message.from_user.id, message.message_id)

        bot.send_message(message.chat.id, text = "Сообщение успешно отправлено✅")
        sleep(2)
        bot.send_message(message.chat.id, text = """<b>🔥🔥🔥ВНИМАНИЕ! Впервые в секторе рекламы!

📌Теперь вы можете мгновенно публиковать свои объявления на нашем канале.
</b>
📡Размещай свои объявления сразу на канале и в нашем чате с закреплением через нашего бота: @textreception_bot

https://t.me/firechannel1
""" ,parse_mode='HTML' )
    else:
        bot.send_message(message.chat.id, text = "<b>❌Длина текста должно быть не менее 20 симболов.❌</b>\n\nПопробуйте ещё раз📝", parse_mode = 'HTML')




@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data.startswith("yes"):
        #bot.send_message(call.message.chat.id, text = "Хорошо, напишите текст ( Можете использовать ссылки, емодзи, и т.д )")
        global ID
        ID = str(call.data.replace("yes","")) # ID клиента

        s = bot.send_message(call.message.chat.id, text = "Напишите текст поста...📝")

        bot.register_next_step_handler(s,reply_msg) # Переходим в reply_msg



    elif call.data == "no":
        bot.send_message(call.message.chat.id, text = "Хорошо, если передумаете - напишите, я всегда тут!🤖")




bot.polling()
