
from func import *

from aiogram.dispatcher.filters import Command

import logging
import asyncio

logging.basicConfig(
    level=logging.DEBUG,
    filename="mylog.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)

logging.info('Hello')



YOUTOKEN = "390540012:LIVE:28953"
# TOKEN = ('5648421216:AAFhRPUQw0FQ6tGkxjyR-Y8TeYMGuhs68OA')
TOKEN = ('5954410335:AAFKiIGDT1VTsgKuNvLgTsrKV-YwgmUdM-o')
Configuration.account_id =  506751
Configuration.secret_key ='538350'
logging.basicConfig(level=logging.INFO)


storage = MemoryStorage()


message__i = {}

async def add_and_clear_message(chat_id, message_id):
    global message__i
    if message__i.get(chat_id) == None:
        message__i[chat_id] = []
    message__i[chat_id].clear()
    message__i[chat_id].append(message_id)


async def add_message(chat_id, message_id):
    global message__i
    if message__i.get(chat_id) == None:
        message__i[chat_id] = []
    message__i[chat_id].append(message_id)


async def delete_message(id):
    global message__i
    if message__i.get(id) != None:
        for i in message__i[id]:

            await bot.delete_message(id, (i))
        message__i[id].clear()


async def send_m(self, chat_id, message, reply_markup=None):

   qq = await self.send_message(chat_id, message, reply_markup=reply_markup)
   await add_message(chat_id, qq.message_id)




Bot.send_m = send_m
bot = Bot(token = TOKEN)

offset = dict()
srcpic = {}
srcvid = {}
srcaud = {}
srctex = {}
firstname = {}
st = {}
ui = {}
link = 0
pic = 0
link_caption ={}
link_url={}
mmessage=''
file_id1 = {}
cir = 0
errors = 0
invois = {}

async def clean1(vi):
   os.remove(vi)


async def clean(vi, vi2):
   os.remove(vi)
   os.remove(vi2)
   
async def cleanall(vi, vi2, au):
   os.remove(vi)
   os.remove(vi2)
   os.remove(au)
class clientState(StatesGroup):
    start = State()
    videost = State()
    audiost = State()
    otmenst = State()
    vremst = State()
    otmen = State()
    q1=  State()
    q11 = State()
    q12 = State()
    smm = State()
    smmq = State()
    smmq1 = State()
    smm_pic = State()
    smm2 = State()
    smm_link = State()
    smm_nolink = State()
    smm_link1 = State()
    smm_link2 = State()
    smmq2 = State()
    done= State()
    smmq3 = State()



    # 
dp = Dispatcher(bot, storage=storage)


db = Database("dataBase.db")

def days_to_sec(days):
    return days * 24 * 60 * 60
def time_sub_day(get_time):
    time_now = int(time.time())
    midlle = int(get_time) - time_now
    if midlle<=0:
        return False
    else:
        dt= str(datetime.timedelta(seconds=midlle))
        dt = dt.replace('days', 'дней')
        dt = dt.replace('day', 'день')
        return dt 




@dp.message_handler(commands=['smm'], state="*")
async def smm(message: types.Message):
    global link
    global pic
    link = 0
    pic = 0
    if message.chat.type == 'private':
        if message.from_user.id == 1340988413:
            await clientState.smm.set()


            await bot.send_message(1340988413, 'Напиши текст для рассылки', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=clientState.smm)
async def replay_smm1(message: Message):
    global mmessage
    if message.chat.type == 'private':
        if message.from_user.id == 1340988413:
            await clientState.smmq1.set()
            mmessage = message.text
            await bot.send_message(1340988413, f"Будет фото?", reply_markup=nav.sub_inline_audio)

@dp.callback_query_handler(text=('yes_btn', 'no_btn'), state=clientState.smmq1)
async def ssmQ(call: types.CallbackQuery):
    global mmessage
    global pic
    if call.data == 'yes_btn':
        if call.message.chat.type == 'private':
            pic = 1
            await bot.delete_message(call.from_user.id, call.message.message_id)
            
            await bot.send_message(1340988413, 'Окей отправь мне фото')
            await clientState.smm_pic.set()
    elif call.data == 'no_btn':
        await clientState.smmq2.set()

        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_message(1340988413, 'Укажем ссылку кнопкой?', reply_markup=nav.sub_inline_audio)


@dp.message_handler(content_types = ContentType.PHOTO, state=clientState.smm_pic)
async def smm_pic(message: Message):
    global srcpic
    global file_id1
    file_id1 = message.photo[-1].file_id
    # file = await bot.get_file(file_id)
    # srcpic[message.chat.id] = f"smm{message.chat.id}.jpg"
    # await bot.download_file(file.file_path, srcpic[message.chat.id])
    await clientState.smmq2.set()
    await bot.send_message(1340988413, 'Окей\nУкажем ссылку кнопкой?', reply_markup=nav.sub_inline_audio)

@dp.callback_query_handler(text=('yes_btn', 'no_btn'), state=clientState.smmq2)
async def ssmQ1(call: types.CallbackQuery):
    global mmessage
    global link
    if call.data == 'yes_btn':
        if call.message.chat.type == 'private':
            link = 1
            await bot.delete_message(call.from_user.id, call.message.message_id)

            await bot.send_message(1340988413, 'Отправь описание кнопки', )
            await clientState.smm_link1.set()
    elif call.data == 'no_btn':
        await clientState.done.set()
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_message(1340988413,  "Нажми на кнопку ниже", reply_markup=nav.backout45)
        

@dp.message_handler(state=clientState.smm_link1)
async def replay_smm(message: Message):
    global mmessage
    global link_caption
    if message.chat.type == 'private':
        if message.from_user.id == 1340988413:
            await clientState.smm_link2.set()
            link_caption = message.text
            await bot.send_message(1340988413, f"Отправить url", )


# @dp.message_handler(state=clientState.smm_link1)
# async def replay_smm(message: Message):
#     global mmessage
#     global link_caption
#     if message.chat.type == 'private':
#         if message.from_user.id == 1340988413:
#             await clientState.smmq.set()
#             link_caption = message.text
#             await bot.send_message(1340988413, f"Отправить url", )


@dp.message_handler(state=clientState.smm_link2)
async def replay_smm2(message: Message):
    global mmessage
    global link_caption
    global link_url
    global srcpic
    if message.chat.type == 'private':
        if message.from_user.id == 1340988413:
            await clientState.done.set()
            link_url = message.text
            await bot.send_message(1340988413, "Нажми на кнопку ниже", reply_markup=nav.backout45)


@dp.message_handler(state=clientState.done)
async def publick(message: Message):
    global link
    global pic
    global mmessage
    global link_caption
    global link_url
    global srcpic
    global file_id1
    
    if message.text == 'Done':
        await clientState.smmq3.set()
        await bot.delete_message(message.from_user.id, (message.message_id-1))
        if pic == 1:
            if link == 1:
                await bot.send_photo(1340988413, photo=file_id1, caption=mmessage, reply_markup=nav.link_smm(link_caption, link_url))
                await bot.send_message(1340988413, "Publick?", reply_markup=nav.sub_inline_audio)
            elif link == 0:
                await bot.send_photo(1340988413, photo=file_id1, caption=mmessage)
                await bot.send_message(1340988413, "Publick?", reply_markup=nav.sub_inline_audio)
        elif pic == 0:
                if link == 1:
                    await bot.send_message(1340988413,  f"{mmessage}", reply_markup=nav.link_smm(link_caption, link_url))
                    await bot.send_message(1340988413, "Publick?", reply_markup=nav.sub_inline_audio)
                elif link == 0:
                    await bot.send_message(1340988413,  f"{mmessage}")
                    await bot.send_message(1340988413, "Publick?", reply_markup=nav.sub_inline_audio)


@dp.callback_query_handler(text=('yes_btn', 'no_btn'), state=clientState.smmq3)
async def ssmQ1(call: types.CallbackQuery):
    global mmessage
    global link
    await bot.delete_message(call.from_user.id, (call.message.message_id-1))

    await bot.delete_message(call.from_user.id, (call.message.message_id))
    if call.data == 'yes_btn':

        users = db.get_users_smm()
        for row in users:
                
            
                if pic == 1:
                    if link == 1:
                        try:
                            await bot.send_photo(row[0], photo=file_id1, caption=mmessage, reply_markup=nav.link_smm(link_caption, link_url))
                            if row[1] != 1:
                                db.set_active(row[0], 1)
                        except:
                            db.set_active(row[0], 0)
                    elif link == 0:
                            try:
                                await bot.send_photo(row[0], photo=file_id1, caption=mmessage)
                                if row[1] != 1:
                                    db.set_active(row[0], 1)
                            except:
                                db.set_active(row[0], 0)

                elif pic == 0:
                        if link == 1:
                            try:
                                await bot.send_message(row[0],  f"{mmessage}", reply_markup=nav.link_smm(link_caption, link_url))
                                if row[1] != 1:
                                    db.set_active(row[0], 1)
                            except:
                                db.set_active(row[0], 0)
                        elif link == 0:
                            try:
                                await bot.send_message(row[0],  f"{mmessage}")
                                if row[1] != 1:
                                    db.set_active(row[0], 1)
                            except:
                                db.set_active(row[0], 0)

        await clientState.start.set()
        await bot.send_message(1340988413, 'Рассылка доставлена\nВы в главном меню', reply_markup=nav.mainMenu)

    elif call.data == 'no_btn':
        await clientState.start.set()
        await bot.send_message(1340988413, '\nВы в главном меню', reply_markup=nav.mainMenu)















    # if call.data == 'yes_btn':
    #     if call.message.chat.type == 'private':

    #         await bot.delete_message(call.from_user.id, call.message.message_id)
    #         if call.from_user.id == 1340988413:

    #             users = db.get_users_smm()
    #             for row in users:
    #                 try:
    #                     await bot.send_photo(1340988413, srcpic[call.chat.id] , caption=mmessage)
    #                     if row[1] != 1:
    #                         db.set_active(row[0], 1)
    #                 except:
    #                     db.set_active(row[0], 0)
    #             await clientState.start.set()
    #             await bot.send_message(1340988413, 'Рассылка доставлена\nВы в главном меню', reply_markup=nav.mainMenu)
    # elif call.data == 'no_btn':
    #     await clientState.start.set()

    #     await bot.delete_message(call.from_user.id, call.message.message_id)
    #     await bot.send_message(1340988413, 'Вы в главном меню', reply_markup=nav.mainMenu)


# @dp.callback_query_handler(text=('yes_btn', 'no_btn'), state=clientState.smm_nolink)
# async def ssmQ(call: types.CallbackQuery):



@dp.message_handler(state=clientState.start)
async def bot_message(message: types.Message, state: FSMContext):
    global srcvid
    global srcaud
    global srctex
    global firstname
    global st
    global ui
    global message__i
    if message.chat.type == 'private':


        if message.text == "Профиль":

            if invois.get(message.from_user.id) != None:
                for i in invois[message.from_user.id]:
                    await bot.delete_message(message.from_user.id, i)
            invois.clear()
            await clientState.otmen.set()
            user_sub = time_sub_day(db.get_time_sub(message.from_user.id))
            if user_sub ==False:
                user_sub = "\nВаш тариф: FREE"
                user = db.get_nickname(message.from_user.id)
                user_nickname = "Ваш ник: " + db.get_nickname(message.from_user.id)
            
                await bot.send_m(message.from_user.id, user_nickname + user_sub, reply_markup=nav.mainMenu1)
                invois[message.from_user.id] = []
                qq = await bot.send_message(message.from_user.id,  'Чтобы пользоваться ботом без ограниченй, предлагаем оформить подписку по кнопке ниже😏', reply_markup=nav.sub_inline)
                invois[message.from_user.id].append(qq.message_id)                
                qq = await bot.send_message(message.from_user.id,  '🎄Новогоднее предложение🎁', reply_markup=nav.sub_inline2)
                invois[message.from_user.id].append(qq.message_id)


            else:
                mes_id_user = message.message_id 
                user_sub = time_sub_day(db.get_time_sub(message.from_user.id))
                user_sub = "\n Тариф: VIP❤️\n Действителен еще " + user_sub
                user_nickname = "Ваш ник: " + db.get_nickname(message.from_user.id)+"🤤"
                await bot.send_m(message.from_user.id, user_nickname + user_sub, reply_markup=nav.mainMenu1)
                
                # message__i = qq.message_id
            

        elif  message.text == "Подписка":
            if invois.get(message.from_user.id) != None:
                for i in invois[message.from_user.id]:
                    await bot.delete_message(message.from_user.id, i)
                invois.clear()
            await clientState.otmen.set()
            if db.get_sub_status(message.from_user.id) == False:
                user_tarif = "Ваш тариф: FREE"
                invois[message.from_user.id]=[]
                await bot.send_m(message.from_user.id, user_tarif, reply_markup=nav.mainMenu1)
                qq = await bot.send_message(message.from_user.id,  'Чтобы пользоваться ботом без ограниченй, предлагаем оформить подписку по кнопке ниже😏', reply_markup=nav.sub_inline)
                invois[message.from_user.id].append(qq.message_id)
                qq = await bot.send_message(message.from_user.id,  '🎄Новогоднее предложение🎁', reply_markup=nav.sub_inline2)
                invois[message.from_user.id].append(qq.message_id)
               

            else:
                user_sub = time_sub_day(db.get_time_sub(message.from_user.id))
                user_sub = "\n Тариф: VIP\n Действителен еще " + user_sub
                await bot.send_m(message.from_user.id,  user_sub, reply_markup=nav.mainMenu1)

        elif message.text == "СОЗДАТЬ КРУГ":
            if invois.get(message.from_user.id) != None:
                for i in invois[message.from_user.id]:
                    await bot.delete_message(message.from_user.id, i)
                invois.clear()
            ui = message.from_user.id
            if db.get_sub_status(message.from_user.id) == False and db.get_free(message.from_user.id) == 0:
                st = False
             
                await bot.send_m(message.from_user.id,  "В вашем тарифе доступны круги до 30 сек.\n\nДавай начнем, отправь мне любое видео☺️", reply_markup=nav.mainMenu1)
                await clientState.videost.set()
            elif db.get_sub_status(message.from_user.id) == True or db.get_free(message.from_user.id) > 0:
                st = True
                await bot.send_m(message.from_user.id,  "В вашем тарифе ограничения отсутсвуют\n\nДавай начнем, отправь мне любое видео☺️", reply_markup=nav.mainMenu1)
                await clientState.videost.set()
        
        elif message.text == "Рефералы":
            if invois.get(message.from_user.id) != None:
                for i in invois[message.from_user.id]:
                    await bot.delete_message(message.from_user.id, i)
                invois.clear()
            await clientState.otmen.set()
            ref=  str(db.get_referal(message.from_user.id))
            ref_free = str(db.get_free(message.from_user.id))
            await bot.send_m(message.from_user.id,  f"Колличесвто приглашенных зайчиков: {ref}\n\nКоличество доступных бесплатных кругов: {ref_free}\n\n\nЧтобы заработать бесплатные круги, пригласи новых участниковв используя эту ссылку\nhttps://t.me/CCircle_bot?start={message.from_user.id}\n\nКак только кто-то зарегистрируется по этой ссылке, ты получишь уведомление❤️" , reply_markup=nav.mainMenu1)
            # await bot.send_message(message.from_user.id, f"Чтобы заработать бесплатные круги, пригласи новых участниковв используя эту ссылку\nhttps://CCircle_bot?start={message.from_user.id}\nКак только кто-то зарегистрируется по этой ссылке, ты получишь уведомление❤️")



@dp.message_handler(state=clientState.otmen)
async def start(message: types):
    global message__i
    global invois
    if message.text == "В главное меню":
        await clientState.start.set()
        if invois.get(message.from_user.id)!= None:
            for i in invois[message.from_user.id]:
                await bot.delete_message(message.from_user.id, i)
            invois.clear()
        await bot.send_message(message.from_user.id, 'Вы в главном меню😏', reply_markup=nav.mainMenu)
        await delete_message(message.from_user.id)
        
        
        # await bot.delete_message(message.from_user.id, (message.message_id-1))
        # await bot.delete_message(message.from_user.id, (message.message_id-2))


# @dp.callback_query_handler(text='submonth', state=clientState.start)
# async def submonth ( call: types.CallbackQuery):
#     global srcvid
#     global srcaud
#     global srctex
#     global firstname
#     await clientState.otmen.set()
    
#     await bot.delete_message(call.from_user.id, message__i[call.from_user.id])
#     # await bot.delete_message(call.from_user.id, call.message.message_id)
#     await bot.send_m(call.from_user.id, 'Во', reply_markup=nav.mainMenu1)
    
#     qq=await bot.send_invoice(chat_id=call.from_user.id, title="Подписка на CCircle", description="данная подписка дает возможность пользоваться ботом целый месяц без ограничейний", payload="month_sub", provider_token=YOUTOKEN, currency="RUB", start_parameter="test_bot", prices=[{"label": "RUB", "amount": 8000}])
#     message__i[call.from_user.id].append(qq.message_id)

@dp.callback_query_handler(text='submonth3', state="*")
async def submonth(call: types.CallbackQuery):
    global srcvid
    global srcaud
    global srctex
    global firstname
    global invois
    await clientState.otmen.set()
    invois.clear()
    await bot.delete_message(call.from_user.id, (call.message.message_id-1))
    await bot.delete_message(call.from_user.id, call.message.message_id)
    
    qq = await bot.send_invoice(chat_id=call.from_user.id, title="Подписка на CCircle", description="данная подписка дает возможность пользоваться ботом целых 3 месяца без ограничейний", payload="month_sub3", provider_token=YOUTOKEN, currency="RUB", start_parameter="test_bot", prices=[{"label": "RUB", "amount": 15000}])
    message__i[call.from_user.id].append(qq.message_id)

@dp.pre_checkout_query_handler(state=clientState.all_states)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.callback_query_handler(text='submonth', state="*")
async def submonth(call: types.CallbackQuery):
    global srcvid
    global srcaud
    global srctex
    global firstname
    global message__i
    await clientState.otmen.set()
    if invois.get(call.from_user.id) != None:
        for i in invois[call.from_user.id]:
           await bot.delete_message(call.from_user.id, i)
        invois.clear()
    else:
        await bot.delete_message(call.from_user.id, (call.message.message_id+1))
        await bot.delete_message(call.from_user.id, call.message.message_id)
    
    await bot.send_m(call.from_user.id, 'Во', reply_markup=nav.mainMenu1)
    
    qq = await bot.send_invoice(chat_id=call.from_user.id, title="Подписка на CCircle", description="данная подписка дает возможность пользоваться ботом целый месяц без ограничейний", payload="month_sub", provider_token=YOUTOKEN, currency="RUB", start_parameter="test_bot", prices=[{"label": "RUB", "amount": 8000}])
    message__i[call.from_user.id].append(qq.message_id)




@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT, state="*")
async def process_pay(message: Message):
    global srcvid
    global srcaud
    global srctex
    global firstname
    if message.successful_payment.invoice_payload == "month_sub":
        
        #подписываем пользователя 
        time_sub = int(time.time()) + days_to_sec(30)
        db.set_time_sub(message.from_user.id, time_sub)
        await clientState.start.set()
        await bot.send_message(message.from_user.id, "Вы подписались на тариф VIP❤️🤤", reply_markup=nav.mainMenu)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT, state="*")
async def process_pay(message: Message):
    global srcvid
    global srcaud
    global srctex
    global firstname
    if message.successful_payment.invoice_payload == "month_sub3":

        # подписываем пользователя
        time_sub = int(time.time()) + days_to_sec(60)
        db.set_time_sub(message.from_user.id, time_sub)
        await clientState.start.set()
        await bot.send_message(message.from_user.id, "Вы подписались на тариф VIP❤️🤤\nНа 3 месяца", reply_markup=nav.mainMenu)





           


@dp.message_handler(content_types=ContentType.VIDEO, state=clientState.videost)
async def check_video(message: Message):
        global srcvid
        global srcaud
        global srctex
        global firstname
        global ui
        global user_nickname

    
        file_id = message.video.file_id 
        if message.video.file_size > 1.7e+7:
            await bot.send_message(message.from_user.id, 'Ох он слишком большой😂\nОтправь видео до 17мб', reply_markup=nav.backout)
          # Get file id
        else:
            file = await bot.get_file(file_id)  # Get file path
            video_number = 0  # Number video file
            # If the file exists, add one to the number

            await bot.send_message(message.from_user.id, 'Отлично☺️!\n ', reply_markup=nav.backout)
            # await asyncio.sleep(20)
            await bot.send_message(message.from_user.id, '\nЖелаешь добвать аудио?', reply_markup=nav.sub_inline_audio)
            user_nickname =   db.get_nickname(message.from_user.id)
            firstname = str(message.from_user.id).format(message.from_user)
            await clientState.q1.set()
            while (os.path.isfile(f"video{video_number}.mp4")):
                video_number += 1
            srcvid[message.chat.id] = f"video{video_number}.mp4"
            await bot.download_file(file.file_path, srcvid[message.chat.id])

            ui = message.from_user.id
        # await bot.send_message(message.from_user.id,'', reply_markup=nav.mainMenu1)


@dp.message_handler(state=clientState.videost)
async def start(message: types):
   
   if message.text == "В главное меню":
        
        await clientState.start.set()
        await bot.send_message(message.from_user.id, 'Вы в главном меню❤️', reply_markup=nav.mainMenu)
        await bot.delete_message(message.from_user.id, (message.message_id-1))
    



@dp.callback_query_handler(text='yes_btn', state=clientState.q1)
async def yes_btn(call: types.CallbackQuery):
    global srcvid
    global srcaud
    global srctex
    global firstname
    await clientState.audiost.set()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    # await bot.send_message(call.message.chat.id, 'Отлично', reply_markup=nav.backout)

    await bot.send_message(call.message.chat.id, 'Отлично\nТеперь отправь мне аудио в формате mp3\nили перешли трек из @mixvk_bot😏', reply_markup=nav.backout)

@dp.callback_query_handler(text= 'no_btn', state=clientState.q1)
async def no_btn(call: types.CallbackQuery):

    await bot.delete_message(call.from_user.id, call.message.message_id)
    global srcvid
    global srcaud
    global srctex
    global firstname
    global st
    global ui
    global cir
    global errors
    global invois
    if st == False and db.get_free(ui) == 0:
        await clientState.start.set()
        await bot.send_message(ui, 'Отлично\nУже загружаю круг 🚛  ', reply_markup=types.ReplyKeyboardRemove())
        # await asyncio.sleep(20)
        na = str(call.message.chat.id) + ".mp4"
        try:
            circleOrig_30(srcvid[call.message.chat.id], na)
        except:

            errors = errors +1
            await bot.send_message(1340988413, f"Ошибка {errors}")
            await bot.send_message(ui, 'Ваше видео битое\nВы в главном меню', reply_markup=nav.mainMenu)
            await clientState.start.set()
            await clean1(srcvid[ui])
        await bot.send_video_note(ui, InputFile(na), reply_markup=nav.mainMenu)
        qq= await bot.send_message(ui,  'Чтобы убрать водяной знак и загружать видео длиной в 1 минуту перейдите на тариф VIP по кнопке ниже😏', reply_markup=nav.sub_inline)
        invois[ui] = []
        invois[ui].append(qq.message_id)
        await bot.send_message(ui, text=krug1(db.get_nickname(ui)))
        
        await bot.send_message(1340988413, f"Был создан круг\nИх уже {db.num_krug(1340988413)}")
        await clean(srcvid[ui], na)
        
    elif st == True or  db.get_free(ui) > 0:
        await clientState.start.set()
        await bot.send_message(ui, 'Отлично\nУже загружаю круг 🚛  ', reply_markup=types.ReplyKeyboardRemove())
        await asyncio.sleep(20)
        na = str(call.message.chat.id) + ".mp4"
        try:
            circleOrig(srcvid[call.message.chat.id], na)
        except:

            errors = errors +1
            await bot.send_message(1340988413, f"Ошибка {errors}")
            await bot.send_message(ui, 'Ваше видео битое\nВы в главном меню', reply_markup=nav.mainMenu)
            await clientState.start.set()
            await clean1(srcvid[ui])
            

        await bot.send_video_note(ui, InputFile(na), reply_markup=nav.mainMenu)
        user = db.get_nickname(ui)
        await bot.send_message(ui, krug1(db.get_nickname(ui)))
        
        await bot.send_message(1340988413, f"Был создан круг\nИх уже {db.num_krug(1340988413)}")
        await clean(srcvid[ui], na)
        k = db.get_free(ui)
        if k > 0:
             db.minus_ref(ui)


@dp.message_handler(state=clientState.audiost)
async def start(message: types.Message):
    global srcvid
    global srcaud
    global srctex
    global firstname
    global st
    global ui

    if message.text == "Назад":

       await clientState.q1.set()
       await bot.delete_message(message.from_user.id, (message.message_id-1))
     
    #    await clean1(srcvid[ui])

       await bot.send_message(message.from_user.id, 'Окей😤', reply_markup=nav.backout)

       await bot.send_message(message.from_user.id, '\nЖелаешь добвать аудио?', reply_markup=nav.sub_inline_audio)

@dp.message_handler(state=clientState.q1)
async def start(message: types.Message):
    global srcvid
    global srcaud
    global srctex
    global firstname
    global st
    global ui

    if message.text == "Назад":
    
       await clientState.videost.set()
       await bot.delete_message(message.from_user.id, (message.message_id-1))
      
       await clean1(srcvid[ui])

       await bot.send_message(message.from_user.id, 'Окей\nПросто оправь мне видео😏', reply_markup=nav.mainMenu1)


@dp.message_handler(content_types=types.ContentType.AUDIO,state=clientState.audiost)
async def xxxxacheck(message: Message):
    global srcvid
    global srcaud
    global srctex
    global firstname

    await bot.delete_message(message.from_user.id,( message.message_id-1))
    await bot.send_message(message.from_user.id, 'Ок получил☺️')
    file_id = message.audio.file_id  # Get file id
    file = await bot.get_file(file_id)  # Get file path
    audio_number = 0  
    await clientState.vremst.set()
    src1 = file.file_path
    srcaud[message.chat.id] = src1
    while (os.path.isfile(f"audio{audio_number}.mp3")):
        audio_number += 1
    srcaud[message.chat.id] = f"audio{audio_number}.mp3"
    await bot.download_file(file.file_path, srcaud[message.chat.id])
    await bot.send_message(message.from_user.id, '\nВыберите фрагмент трека,  с какой секунды его начать\nнапишите цифрой', reply_markup=nav.backout)

        
        
@dp.message_handler(state=clientState.audiost)
async def start(message: types.Message):

   if message.text == "В главное меню":

        await bot.delete_message(message.from_user.id, message.message_id)
        await clientState.start.set()
        await bot.send_message(message.from_user.id, 'Вы в главном меню😍', reply_markup=nav.mainMenu)


@dp.message_handler(state=clientState.vremst)
async def get_sec(message: Message):
    global srcvid
    global srcaud
    global srctex
    global firstname
    global cir
    global errors
    global invois
    await bot.delete_message(message.from_user.id, (message.message_id-1))
    if message.text == "Назад":
        await clientState.q1.set()
        await clean1(srcaud[ui])
        await bot.send_message(message.from_user.id, 'Окей😏', reply_markup=nav.backout)
        await bot.send_message(message.from_user.id, '\nЖелаешь добвать аудио?', reply_markup=nav.sub_inline_audio)
    elif message.text.isdigit() == True:
        if db.get_sub_status(message.from_user.id) == False and db.get_free(message.from_user.id) == 0:

            await bot.send_message(message.chat.id, 'Отлично\nУже загружаю круг🚛❤️ ', reply_markup=types.ReplyKeyboardRemove())
            await asyncio.sleep(20)
            na = str(message.chat.id) + ".mp4"
            srctex[message.chat.id] = int(message.text)
            try:
                circle_30(srcvid[message.chat.id], na, srcaud[message.chat.id], srctex[message.chat.id])
            except:

                errors = errors +1
                await bot.send_message(1340988413, f"Ошибка {errors}")
                await bot.send_message(ui, 'Ваше видео битое\nВы в главном меню', reply_markup=nav.mainMenu)
                await clientState.start.set()
                await clean(srcvid[ui],srcaud[ui])
            await bot.send_video_note(message.from_user.id, InputFile(na), reply_markup=nav.mainMenu)
            await cleanall(srcvid[ui], na, srcaud[ui])

            
            await bot.send_message(1340988413, f"Был создан круг\nИх уже {db.num_krug(1340988413)}")
            qq=await bot.send_message(message.from_user.id,  'Чтобы убрать водяной знак и загружать видео длиной в 1 минуту перейдите на тариф VIP по кнопке ниже😏', reply_markup=nav.sub_inline)
            invois[message.from_user.id] = []
            invois[message.from_user.id].append(qq.message_id)
            await bot.send_message(message.from_user.id, text=krug1(db.get_nickname(message.from_user.id)))
            await clientState.start.set()
        else:

            await bot.send_message(message.chat.id, 'Отлично\nУже загружаю круг🚛❤️ ', reply_markup=types.ReplyKeyboardRemove())
            await asyncio.sleep(20)
            na = str(message.chat.id) + ".mp4"
            srctex[message.chat.id] = int(message.text)
            try:
                circle_60(srcvid[message.chat.id], na,
                    srcaud[message.chat.id], srctex[message.chat.id])
            except:
                errors = errors +1
                await bot.send_message(1340988413, f"Ошибка {errors}")
                await bot.send_message(ui, 'Ваше видео битое\nВы в главном меню', reply_markup=nav.mainMenu)
                await clientState.start.set()
                await clean(srcvid[ui], srcaud[ui])
            await bot.send_video_note(message.from_user.id, InputFile(na), reply_markup=nav.mainMenu)
            await bot.send_message(message.from_user.id, text=krug1(db.get_nickname(message.from_user.id)))

            
            await bot.send_message(1340988413, f"Был создан круг\nИх уже {db.num_krug(1340988413)}")
            await cleanall(srcvid[ui], na, srcaud[ui])
            if db.get_free(message.from_user.id) > 0:
                db.minus_ref(message.from_user.id)
            await clientState.start.set()
    
    else:
        await bot.send_message(message.from_user.id, "Просто напиши цифру😤")





       

@dp.message_handler(state=clientState.vremst)
async def start(message: types.Message):

   if message.text == "Назад":
       await clientState.q1.set()
       await bot.send_message(message.from_user.id, 'Вы в главном меню', reply_markup=nav.mainMenu)










@dp.message_handler(state=None)
async def start(message: types.Message):
    if message.chat.type == 'private':
        global srcvid
        global srcaud
        global srctex
        global firstname
        if "/start" in message.text:
            if (not db.user_exists(message.from_user.id)):
                start_command = message.text
                referal_id = str(start_command[7:])
                if str(referal_id) != '':

                    db.add_user(message.from_user.id, referal_id)
                    db.set_ref(referal_id)
                    await bot.send_message(referal_id, "У вас новый реферал, а это значит что вы можете создать круг бесплатно\n\nКоличество рефералов вы можете увидеть в главном меню, на вкладке рефералы")
                else:
                    db.add_user(message.from_user.id)
                await bot.send_message(message.from_user.id, 'Укажите свой ник, только латинскими буквами', reply_markup=types.ReplyKeyboardRemove())

            else:
                await bot.send_message(message.from_user.id, 'Вы уже зарегестрированны', reply_markup=nav.mainMenu)
                await clientState.start.set()
        else:
            if db.get_signup(message.from_user.id) == "setnickname":
                if (len(message.text) > 15):
                        await bot.send_message(message.from_user.id, 'Ник не должен превышать 15 символов')
                elif "@" in message.text or "/" in message.text:
                        await bot.send_message(message.from_user.id, 'Хватит использовать запрещенные символы')
                else:
                        db.set_nickname(message.from_user.id, message.text)
                        db.set_signup(message.from_user.id, "Done")
                        await clientState.start.set()
                        await bot.send_message(message.from_user.id, "вы завершили регистрацию", reply_markup=nav.mainMenu)
            else:
                await bot.send_message(message.from_user.id, "И что это может значить?", reply_markup=nav.mainMenu)
                await bot.send_message(message.from_user.id, "Теперь вы в главном меню\nПопробуй снова")
                await clientState.start.set()






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

