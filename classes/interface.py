from aiogram.types import *
from .constant import *


# Куаныш микрорайон, 17
# Алматы, Ауэзовский район
# https://go.2gis.com/i0trd

class Interface():
    def __init__(self,language = True):
        self.language = language

    def welcome(self):

        welcome_animation = 'static/animations/welcome.tgs'
        
        welcome_message = {
            True  : """
            <b>
            Сәлем {0}🤗, менің атым @yqylasfilmsbot
            .....
            </b>
            """,
            False : """
            <b>
            Привет {0}🤗, меня зовут @yqylasfilmsbot
            </b>
            """
        }
        
        
        welcome_keyboard = ReplyKeyboardMarkup(keyboard=[
            [WELCOME_LANGUAGE[self.language][0]],
            [WELCOME_LANGUAGE[self.language][1],WELCOME_LANGUAGE[self.language][2]],
            [WELCOME_LANGUAGE[self.language][3],WELCOME_LANGUAGE[self.language][4]],
            [WELCOME_LANGUAGE[self.language][5],WELCOME_LANGUAGE[self.language][6]],
            # [WELCOME_LANGUAGE[self.language][7]]
        ],  resize_keyboard=True,one_time_keyboard=False
        )

        return welcome_animation, welcome_message[self.language], welcome_keyboard

    def start(self):

        start_message = "<b>Интерфейс тілін таңдаңыз\n----------------------------------------\nВыберите язык интерфейса</b>"

        start_keyboard = ReplyKeyboardMarkup(
            keyboard = [[list(INTERFACE_LANGUAGE.keys())[0]], [list(INTERFACE_LANGUAGE.keys())[1]]],
            resize_keyboard=True,
            one_time_keyboard=True
        )
        return start_message, start_keyboard

    def office_address(self):
        return ADDRESS_TEXT[self.language], [43.209661,76.856789]

    def about_us(self):
        
        return 'static/img/logotype.jpeg', ABOUT_US[self.language]

    def send_price(self):
        keyboard = ReplyKeyboardMarkup(keyboard=[[LOVESTORY_KEYBOARD[0]],[LOVESTORY_KEYBOARD[1]],[LOVESTORY_KEYBOARD[2]],[LOVESTORY_KEYBOARD[3]]],resize_keyboard=True)
        return open('static/files/price.pdf', 'rb'),keyboard
    
    def each_price(self,price):
        return PRICE_KEYBOARD[price][0],PRICE_KEYBOARD[price][1][self.language]
        
        
        


    # --------Quiz section⬇️
    def importance(self):

        importance_photo = 'static/questions/q1.jpg'

        importance_message = {
            True : """<b>Сіз үшін LoveStory-де не маңызды?</b>""",
            False : """<b>Что для вас важнее в LoveStory?</b>"""
        }

        importance_keybard = {
            True  : InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Сценарий🕺',callback_data=VARIATIONS[CATEGORIES[0]][0]),InlineKeyboardButton(text='Образ🎭',callback_data=VARIATIONS[CATEGORIES[0]][1])],[InlineKeyboardButton(text='Локация🏕',callback_data=VARIATIONS[CATEGORIES[0]][2])]]),
            False : InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Сценарий🕺',callback_data=VARIATIONS[CATEGORIES[0]][0]),InlineKeyboardButton(text='Образ🎭',callback_data=VARIATIONS[CATEGORIES[0]][1])],[InlineKeyboardButton(text='Локация🏕',callback_data=VARIATIONS[CATEGORIES[0]][2])]])
        }        

        return importance_photo,importance_message[self.language],importance_keybard[self.language]


    def style(self):

        style_photo = 'static/questions/q2.jpg'

        style_message = {
            True  : """<b>Сізге қандай түсіру стильі ұнайды?</b>""",
            False : """<b>Какой стиль съемки вам больше нравится?</b>"""
        }

        style_keybard = {
            True  : InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Классикалық👫',callback_data=VARIATIONS[CATEGORIES[1]][0]),InlineKeyboardButton(text='Динамикалық🏇',callback_data=VARIATIONS[CATEGORIES[1]][1])],[InlineKeyboardButton(text='Экстремалды🏄‍♂️',callback_data=VARIATIONS[CATEGORIES[1]][2])]]),
            False : InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Классический👫',callback_data=VARIATIONS[CATEGORIES[1]][0]),InlineKeyboardButton(text='Динамичный🏇',callback_data=VARIATIONS[CATEGORIES[1]][1])],[InlineKeyboardButton(text='Эктремальный🏄‍♂️',callback_data=VARIATIONS[CATEGORIES[1]][2])]])
        }        

        return style_photo, style_message[self.language], style_keybard[self.language]


    def form(self):
        
        form_photo = 'static/questions/q3.jpg'

        form_message = {
            True  : """<b>Сізге қандай образ ыңғайлы?</b>""",
            False : """<b>Какой образ вам больше по душе?</b>"""
        }

        form_keybard = {
            True  : InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Этно🧥',callback_data=VARIATIONS[CATEGORIES[2]][0]),InlineKeyboardButton(text='Классика🍷',callback_data=VARIATIONS[CATEGORIES[2]][1])],[InlineKeyboardButton(text='Артхаус👩‍🎨',callback_data=VARIATIONS[CATEGORIES[2]][2])]]),
            False : InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Этно🧥',callback_data=VARIATIONS[CATEGORIES[2]][0]),InlineKeyboardButton(text='Классика🍷',callback_data=VARIATIONS[CATEGORIES[2]][1])],[InlineKeyboardButton(text='Артхаус👩‍🎨',callback_data=VARIATIONS[CATEGORIES[2]][2])]])
        }        

        return form_photo, form_message[self.language], form_keybard[self.language]


    def producer(self):
        
        producer_photo = 'static/questions/q4.jpg'

        producer_message = {
            True  : """<b>Сценарийді кім құрады?</b>""",
            False : """<b>Кто придумывает идею сценария?</b>"""
        }

        producer_keybard = {
            True  : InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Мен',callback_data=VARIATIONS[CATEGORIES[3]][0]),InlineKeyboardButton(text='Сіз',callback_data=VARIATIONS[CATEGORIES[3]][1])],[InlineKeyboardButton(text='Бірге',callback_data=VARIATIONS[CATEGORIES[3]][2])]]),
            False : InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Я',callback_data=VARIATIONS[CATEGORIES[3]][0]),InlineKeyboardButton(text='Вы',callback_data=VARIATIONS[CATEGORIES[3]][1])],[InlineKeyboardButton(text='Вместе',callback_data=VARIATIONS[CATEGORIES[3]][2])]])
        }        

        return producer_photo, producer_message[self.language], producer_keybard[self.language]


    def location(self):
        
        location_photo = 'static/questions/q5.jpg'

        location_message = {
            True  : """<b>Түсірілім локациясын таңдаңыз?</b>""",
            False : """<b>Выберите место для съемки?</b>"""
        }

        location_keybard = {
            True  : InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Табиғат🏔',callback_data=VARIATIONS[CATEGORIES[4]][0]),InlineKeyboardButton(text='Қала🏙',callback_data=VARIATIONS[CATEGORIES[4]][1])],[InlineKeyboardButton(text='Студия📸',callback_data=VARIATIONS[CATEGORIES[4]][2])]]),
            False : InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Природа🏔',callback_data=VARIATIONS[CATEGORIES[4]][0]),InlineKeyboardButton(text='Город🏙',callback_data=VARIATIONS[CATEGORIES[4]][1])],[InlineKeyboardButton(text='Студия📸',callback_data=VARIATIONS[CATEGORIES[4]][2])]])
        }        
        
        return location_photo, location_message[self.language], location_keybard[self.language]


    def price(self):
        
        price_photo = 'static/questions/q6.jpg'

        price_message = {
            True  : """<b>Түсірілімді қанша суммаға жоспарлап отырсыз?</b>""",
            False : """<b>На какую сумму вы расчитываете?</b>"""
        }
        
        price_keybard = {
            True  : InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='100-150 мың',callback_data=VARIATIONS[CATEGORIES[5]][0]),InlineKeyboardButton(text='150-300 мың',callback_data=VARIATIONS[CATEGORIES[5]][1])],[InlineKeyboardButton(text='300 мың және жоғары',callback_data=VARIATIONS[CATEGORIES[5]][2])]]),
            False : InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='100-150 тыс.',callback_data=VARIATIONS[CATEGORIES[5]][0]),InlineKeyboardButton(text='150-300 тыс.',callback_data=VARIATIONS[CATEGORIES[5]][1])],[InlineKeyboardButton(text='от 300 тыс. и выше',callback_data=VARIATIONS[CATEGORIES[5]][2])]])
        }        
        
        return price_photo, price_message[self.language], price_keybard[self.language]


    def season(self):
        
        season_photo = 'static/questions/q7.jpg'

        season_message = {
            True   : """<b>Тойыңыз қай мезгілде?💍</b>""",
            False  : """<b>Когда у вас свадьба?💍</b>""",
        }

        season_keybard = {
            True  : InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Көктем🏞',callback_data=VARIATIONS[CATEGORIES[6]][0]),InlineKeyboardButton(text='Жаз☀️',callback_data=VARIATIONS[CATEGORIES[6]][1])],[InlineKeyboardButton(text='Күз🍁',callback_data=VARIATIONS[CATEGORIES[6]][2]),InlineKeyboardButton(text='Қыс☃️',callback_data=VARIATIONS[CATEGORIES[6]][3])]]),
            False : InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Весна🏞',callback_data=VARIATIONS[CATEGORIES[6]][0]),InlineKeyboardButton(text='Лето☀️',callback_data=VARIATIONS[CATEGORIES[6]][1])],[InlineKeyboardButton(text='Весна🍁',callback_data=VARIATIONS[CATEGORIES[6]][2]),InlineKeyboardButton(text='Зима☃️',callback_data=VARIATIONS[CATEGORIES[6]][3])]])
        }

        return season_photo, season_message[self.language], season_keybard[self.language]


    def contact(self):

        contact_photo = 'static/img/contact.jpg'

        contact_message = {
            True  : """<b>Телефон нөмеріңізді жіберіңіз. Және біз жауаптарыңызға байланысты сізге тегін консультация жүргізетін боламыз. 🤗</b>""",
            False : """<b>Оставьте свой номер телефона. И мы бесплатно проконсультируем вас в зависимости от ваших ответов.  🤗</b>"""
        }

        contact_keyboard = {
            True  : ReplyKeyboardMarkup(keyboard=[[KeyboardButton('Жіберу📞',request_contact=True)]],resize_keyboard=True),
            False : ReplyKeyboardMarkup(keyboard=[[KeyboardButton('Отправить📞',request_contact=True)]],resize_keyboard=True)
        }

        return contact_photo, contact_message[self.language], contact_keyboard[self.language]        
        

