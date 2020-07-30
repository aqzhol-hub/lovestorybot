from aiogram import Bot, Dispatcher, executor
from aiogram.types import *
# from table import *
# from lister import interface_language,variations,categories

from classes.database import Database
from classes.interface import Interface
from classes.constant import *



# -------------Connection
dbname = 'puttgvir'
user = 'puttgvir'
password = 'scuWJvr8CgsuGpkzgyC3YBsHVdz7cbED'
host = 'rogue.db.elephantsql.com'
port = '5432'

# -------------Classes
interface = Interface()
database = Database(dbname,user,password,host,port)




# -------------Bot
# TOKEN = '1251528088:AAECXGaHJx7J7PsDPKsot5rpWlThNN-hpuw'
# TOKEN = '1300236281:AAFhQKebBujEHIlNN43r7xQ2YKtqWWzyy78'
TOKEN = '1265307353:AAEZHrSyw6-AhWyXrZvMMuc0zxzYa2jGOD8'
bot = Bot(TOKEN)
dp = Dispatcher(bot)



# -------------Functions
async def send_photo(chat_id,photo = 'static/img/logotype.jpeg',caption=None,keyboard=None):
    await bot.send_photo(chat_id=chat_id,photo=open(photo,'rb'),caption=caption,parse_mode='html',reply_markup=keyboard)


# -------------Dispachers
@dp.message_handler(commands = ['start'])
async def start(message : Message):
    global database
    text, keyboard = interface.start()
    await bot.send_message(chat_id=message.chat.id,text=text,parse_mode='html',reply_markup=keyboard)
    database.add_client(message.chat.id,message.from_user.first_name,message.chat.last_name,message.from_user.username)
    


@dp.message_handler(content_types = ['text'])
async def text(message : Message):

    # --------Global variables
    global interface
    global database

    # --------Set interface language
    if message.text in INTERFACE_LANGUAGE.keys():
        interface = Interface(INTERFACE_LANGUAGE[message.text])

        animation, text, keyboard = interface.welcome()
        await bot.send_animation(chat_id=message.chat.id,animation = open(animation,'rb'))
        await bot.send_message(chat_id=message.chat.id, text = text.format(message.from_user.first_name),parse_mode='html',reply_markup=keyboard)


    # --------Keyboard listener
    if message.text in list(WELCOME_LANGUAGE.values())[0] or list(WELCOME_LANGUAGE.values())[1]:
        if   message.text == WELCOME_LANGUAGE[interface.language][0]:
            photo, caption = interface.about_us()
            await send_photo(message.chat.id,photo=photo)
            await bot.send_message(message.chat.id,text =caption,parse_mode='html')
            
        elif message.text == WELCOME_LANGUAGE[interface.language][1]:# start_quiz
            photo,caption,keyboard = interface.importance()
            database.add_quiz(message.chat.id)
            await send_photo(message.chat.id,photo,caption,keyboard)
            
        elif message.text == WELCOME_LANGUAGE[interface.language][2]:
            await bot.send_message(message.chat.id,database.get_works(),parse_mode='html')
            pass
        elif message.text == WELCOME_LANGUAGE[interface.language][3]:#contact
            await bot.send_contact(chat_id=message.chat.id,phone_number='87756508888',first_name='Yqylasfilms', last_name='LoveStory',vcard='19191919191919191919')
            await bot.send_contact(chat_id=message.chat.id,phone_number='87056458888',first_name='Yqylasfilms', last_name='LoveStory',vcard='19191919191919191919')

        elif message.text == WELCOME_LANGUAGE[interface.language][4]:# address
            text,location = interface.office_address()
            await bot.send_message(chat_id=message.chat.id,text=text,parse_mode='html')
            await bot.send_location(chat_id=message.chat.id,latitude=location[0],longitude=location[1])

        elif message.text == WELCOME_LANGUAGE[interface.language][5]:# price_list
            document,keyboard = interface.send_price()
            await bot.send_document(chat_id=message.chat.id,document=document,reply_markup=keyboard)
            
        elif message.text == WELCOME_LANGUAGE[interface.language][6]:
            await start(message)
            
        # elif message.text == WELCOME_LANGUAGE[interface.language][7]:
        #     pass

    if message.text in LOVESTORY_KEYBOARD:
        if message.text != LOVESTORY_KEYBOARD[-1]:
            document, keyboard = interface.send_price()
            photo,text = interface.each_price(message.text)
            await send_photo(message.chat.id,photo,text,keyboard)
        else:
             animation, text, keyboard = interface.welcome()
             await send_photo(chat_id=message.chat.id,keyboard=keyboard)
        
    try:
        await bot.delete_message(message.chat.id, message.message_id)
    except Exception as e:
        print(e)
        

@dp.message_handler(content_types=['contact'])
async def contact(message):
    # --------Global variables
    global interface
    global database

    database.add_contact(message.contact.phone_number,message.chat.id)
    
    animation, text, keyboard = interface.welcome()
    img,text = database.result_client(message.chat.id)
    await send_photo(message.chat.id,img,text,keyboard)
    
    result = database.quiz_result(message.chat.id)
    await bot.send_message(chat_id=message.chat.id,text=result,parse_mode='html',reply_markup=None)
    



# -------------CallBackQueries
@dp.callback_query_handler(lambda call : True)
async def callback_query_handler(call : CallbackQuery):
    
    # ---------Global variables
    global database
    
    # ---------Quiz listener
    if call.data in [i for i in list(VARIATIONS.values()) if call.data in i][0]:

        if   call.data in VARIATIONS[CATEGORIES[0]]:# importance
            photo,caption,keyboard = interface.style()
            await send_photo(call.message.chat.id,photo,caption,keyboard)

        elif call.data in VARIATIONS[CATEGORIES[1]]:# style
            photo,caption,keyboard = interface.form()
            await send_photo(call.message.chat.id,photo,caption,keyboard)
            
        elif call.data in VARIATIONS[CATEGORIES[2]]:# form
            photo,caption,keyboard = interface.producer()
            await send_photo(call.message.chat.id,photo,caption,keyboard)
            
        elif call.data in VARIATIONS[CATEGORIES[3]]:# producer
            photo,caption,keyboard = interface.location()
            await send_photo(call.message.chat.id,photo,caption,keyboard)
            
        elif call.data in VARIATIONS[CATEGORIES[4]]:# location
            photo,caption,keyboard = interface.price()
            await send_photo(call.message.chat.id,photo,caption,keyboard)
            
        elif call.data in VARIATIONS[CATEGORIES[5]]:# price
            photo,caption,keyboard = interface.season()
            await send_photo(call.message.chat.id,photo,caption,keyboard)

        elif call.data in VARIATIONS[CATEGORIES[6]]:# season
            photo,caption,keyboard = interface.contact()
            await send_photo(call.message.chat.id,photo,caption,keyboard)
            
            
    database.add_client_liking(call.message.chat.id,call.data)
    await bot.delete_message(call.message.chat.id,call.message.message_id)
    
    
    




# -------------Driver
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)
