from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


btnProfile = KeyboardButton ('Профиль')
btnSub = KeyboardButton ('Подписка')
sozdatbtn = KeyboardButton('СОЗДАТЬ КРУГ')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnProfile, btnSub, sozdatbtn)

# ______________________________
btnout = KeyboardButton('В главное меню')
mainMenu1 = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu1.add(btnout)

btnout = KeyboardButton('Назад')
backout = ReplyKeyboardMarkup(resize_keyboard=True)
backout.add(btnout)




sub_inline = InlineKeyboardMarkup(row_width=1)
btn_SubmMonth = InlineKeyboardButton( text= " 1 Месяц за 80 руб", callback_data="submonth")

sub_inline.insert(btn_SubmMonth)


sub_inline_audio = InlineKeyboardMarkup(row_width=0.5)
yesbtn = InlineKeyboardButton( text= "Конечно", callback_data="yes_btn")
nobtn = InlineKeyboardButton(text="Не нужно", callback_data="no_btn")

sub_inline_audio.add(yesbtn, nobtn)

