from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

refer = KeyboardButton('Рефералы')
btnProfile = KeyboardButton ('Профиль')
btnSub = KeyboardButton ('Подписка')
sozdatbtn = KeyboardButton('СОЗДАТЬ КРУГ')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnProfile, btnSub, sozdatbtn, refer)

# ______________________________
btnout = KeyboardButton('В главное меню')
mainMenu1 = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu1.add(btnout)

btnout = KeyboardButton('Назад')
backout = ReplyKeyboardMarkup(resize_keyboard=True)
backout.add(btnout)

btnoutdone = KeyboardButton('Done')
backout45 = ReplyKeyboardMarkup(resize_keyboard=True)
backout45.add(btnoutdone)




sub_inline = InlineKeyboardMarkup(row_width=1)
btn_SubmMonth = InlineKeyboardButton( text= "1 Месяц за 80 руб", callback_data="submonth")

sub_inline.add(btn_SubmMonth)

sub_inline2 = InlineKeyboardMarkup(row_width=1)
btn_SubmMonth3 = InlineKeyboardButton( text= "🔥3 МЕСЯЗА ЗА 150 руб🔥", callback_data="submonth3")

sub_inline2.add( btn_SubmMonth3)


sub_inline_audio = InlineKeyboardMarkup(row_width=0.5)
yesbtn = InlineKeyboardButton( text= "Конечно", callback_data="yes_btn")
nobtn = InlineKeyboardButton(text="Не нужно", callback_data="no_btn")

sub_inline_audio.add(yesbtn, nobtn)

def link_smm(text1, url1):
    linkurldone= InlineKeyboardMarkup(row_width=1)
    link_url = InlineKeyboardButton( text=text1, url=url1)
    return linkurldone.add(link_url)

