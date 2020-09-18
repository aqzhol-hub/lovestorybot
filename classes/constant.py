
# -------------KEYBOARD
CATEGORIES = ['importance', 'style', 'form', 'producer', 'location', 'price','season']

VARIATIONS = {
        CATEGORIES[0] : ['scenario', 'formal',   'location' ],   # importance
        CATEGORIES[1] : ['classic',  'dynamic',  'extremely'],   # style
        CATEGORIES[2] : ['ethno',    'classica', 'arthouse' ],   # form
        CATEGORIES[3] : ['me',       'you',      'together' ],   # producer
        CATEGORIES[4] : ['city',     'nature',   'studio'   ],   # location
        CATEGORIES[5] : ['100-150',  '150-300',  '300'      ],   # price
        CATEGORIES[6] : ['spring', 'summer','fall', 'winter'],   # season
}

CHOICES = {
    VARIATIONS[CATEGORIES[0]][0]:'Сценарий🕺',
    VARIATIONS[CATEGORIES[0]][1]:'Образ🎭',
    VARIATIONS[CATEGORIES[0]][2]:'Локация🏕',

    VARIATIONS[CATEGORIES[1]][0]:'Классикалық👫',
    VARIATIONS[CATEGORIES[1]][1]:'Динамикалық🏇',
    VARIATIONS[CATEGORIES[1]][2]:'Экстремалды🏄‍♂️',

    VARIATIONS[CATEGORIES[2]][0]:'Этно🧥',
    VARIATIONS[CATEGORIES[2]][1]:'Классика🍷',
    VARIATIONS[CATEGORIES[2]][2]:'Артхаус👩‍🎨',

    VARIATIONS[CATEGORIES[3]][0]:'Мен',
    VARIATIONS[CATEGORIES[3]][1]:'Сіз',
    VARIATIONS[CATEGORIES[3]][2]:'Бірге',
    
    VARIATIONS[CATEGORIES[4]][0]:'Табиғат🏔',
    VARIATIONS[CATEGORIES[4]][1]:'Қала🏙',
    VARIATIONS[CATEGORIES[4]][2]:'Студия📸',

    VARIATIONS[CATEGORIES[5]][0]:'100-150 мың',
    VARIATIONS[CATEGORIES[5]][1]:'150-300 мың',
    VARIATIONS[CATEGORIES[5]][2]:'300 мың және жоғары',

    VARIATIONS[CATEGORIES[6]][0]:'Көктем🏞',
    VARIATIONS[CATEGORIES[6]][1]:'Жаз☀️',
    VARIATIONS[CATEGORIES[6]][2]:'Күз🍁',
    VARIATIONS[CATEGORIES[6]][3]:'Қыс☃️'
}

INTERFACE_LANGUAGE = {'🇰🇿Қазақ тілі' : True,'🇷🇺Русский язык' : False}

WELCOME_LANGUAGE = {
        True  : ['Біз жайлы🎥','Квиз өту🎯','Жұмыстар🎬','Контактілер📞', 'Мекен-жай🏢', 'Прайслист🗒','🇰🇿 🔁 🇷🇺','Кездесуге жазылу👥'],
        False : ['Про нас🎥','Пройти квиз🎯', 'Работы🎬', 'Контакты📞', 'Адрес🏢', 'Прайслист🗒', '🇰🇿 🔁 🇷🇺','Записаться на встречу👥']
}



LOVESTORY_KEYBOARD = ['Classic 167000тг', 'Premium 287000тг', 'Exclusive 497000тг', '⬅']

PRICE_KEYBOARD = {
    LOVESTORY_KEYBOARD[0]:[
        'static/img/classic.jpg',
        {False : """
        <b>Пакет “Classic”</b>

<b>ЧТО ВХОДИТ В ПАКЕТ:</b>
<i>
0/5 Съемочный день (6 часов)
2 локаций в городе
2 образа под стиль
</i>

<b>КТО ОБСЛУЖИВАЕТ:</b>
<i>
1 Фотограф(со светом)
1 Видеограф(со стабом)
</i>

<b>ПОСЛЕ СЪЕМКИ:</b>
<i>
Монтаж видео материала
Цветокоррекция видео
Обработка фотографий
</i>

<b>В ПОДАРОК🎁:</b>
Фирменная флешка 16GB
        """,
        True:"""
<b>“Classic” пакеті</b>

<b>ПАКЕТКЕ НЕ КІРЕДІ:</b>
<i>
1 күндік фото/видео түсірілім ( 8 сағат )
3 локация ( қалада )
6 сцена ( Мини локациялар )
3 түрлі образ-стиль
</i>

<b>КТО ОБСЛУЖИВАЕТ:</b>
<i>
1 Видеограф( стабпен )
1 Пилот ( дронмен )
</i>

<b>ТҮСІРІЛІМНЕН КЕЙІН:</b>
<i>
Видеоның монтажы
Видеоның цветокоррекциясы
Сіздердің түзетулеріңіз
</i>

<b>СЫЙЛЫҚҚА 🎁:</b>
Фирмалық флешка 64 gb
Фото рамка A3 көлемінде ( 1 еу )
Инстаграм ролик ( 1 мин )
        """
        }
    ],
    LOVESTORY_KEYBOARD[1]:
    [
        'static/img/premium.jpg',
        {False : """
        <b>Пакет “Premium”</b>

<b>ЧТО ВХОДИТ В ПАКЕТ:</b>
<i>
1 Съемочный день (12 часов)
3 локаций в городе и с выездом
9 сцены (Мини локаций)
2 образа под стиль
</i>

<b>КТО ОБСЛУЖИВАЕТ:</b>
<i>
1 Фотограф(со светом)
1 Видеограф(со стабом)
1 Пилот (с дроном)
</i>

<b>ПОСЛЕ СЪЕМКИ:</b>
<i>
Монтаж видео материала
Цветокоррекция видео
Обработка фотографий
Поправка с вашей стороны
</i>

<b>В ПОДАРОК🎁:</b>
Фирменная флешка 32GB
Фото рамка в размере А3(1 шт.)
Инстаграм ролик(1 мин)
        """,
        True : """
<b>“Premium” пакеті</b>

<b>ПАКЕТКЕ НЕ КІРЕДІ:</b>
<i>
1 күндік фото/видео түсірілім ( 12 сағат )
3 локация ( қалада және қала сыртында )
9 сцена ( Мини локациялар )
3 түрлі образ-стиль
</i>

<b>КІМ ҚЫЗМЕТ КӨРСЕТЕДІ::</b>
<i>
1 Фотограф( жарықпен )
1 Видеограф( стабпен )
1 Пилот ( дронмен )
</i>

<b>ТҮСІРІЛІМНЕН КЕЙІН:</b>
<i>
Видеоның монтажы
Видеоның цветокоррекциясы
Фотолардың өңделуі
Сіздердің түзетулеріңіз
</i>

<b>СЫЙЛЫҚҚА🎁:</b>
Фирмалық флешка 32 gb
Фото рамка A3 көлемінде ( 2 еу )
Инстаграм ролик ( 1 мин )
        """
        }
    ],
    LOVESTORY_KEYBOARD[2]:[
        'static/img/exclusive.jpg',
        {False : """
        <b>Пакет “Exclusive”</b>

<b>ЧТО ВХОДИТ В ПАКЕТ:</b>
<i>
2 Съемочный день (24 часов)
4 локаций в городе и с выездом
12 сцены (Мини локаций)
4 образа под стиль
</i>

<b>КТО ОБСЛУЖИВАЕТ:</b>
<i>
1 Фотограф(со светом)
1 Видеограф(со стабом)
1 Пилот (с дроном)
1 Видеограф(экшн камера)
</i>

<b>ПОСЛЕ СЪЕМКИ:</b>
<i>
Монтаж видео материала
Цветокоррекция видео
Обработка фотографий
Поправка с вашей стороны
</i>

<b>В ПОДАРОК🎁:</b>
Фирменная флешка 32GB
Фото рамка в размере А3(1 шт.)
Инстаграм ролик(1 мин.)
Видео пригласительный (1 мин.)
        """,
        True:"""
<b>“Premium” пакеті</b>

<b>ПАКЕТКЕ НЕ КІРЕДІ:</b>
<i>
1 күндік фото/видео түсірілім ( 12 сағат )
3 локация ( қалада және қала сыртында )
9 сцена ( Мини локациялар )
3 түрлі образ-стиль
</i>

<b>КІМ ҚЫЗМЕТ КӨРСЕТЕДІ::</b>
<i>
1 Фотограф( жарықпен )
1 Видеограф( стабпен )
1 Пилот ( дронмен )
</i>

ТҮСІРІЛІМНЕН КЕЙІН:
Видеоның монтажы
Видеоның цветокоррекциясы
Фотолардың өңделуі
Сіздердің түзетулеріңіз

СЫЙЛЫҚҚА 🎁:
Фирмалық флешка 64 gb
Фото рамка A3 көлемінде ( 3 еу )
Инстаграм ролик ( 1 мин )
Тойға шақыру видеосы ( 1 мин )
        """
}
    ]
}



# -------------CONSTANT VARIABLES


ADDRESS_TEXT = { 
    True  : """Куаныш ықшамауданы, 17\nАлматы, Әуезов районы\nhttps://go.2gis.com/i0trd""",
    False : """Куаныш микрорайон, 17\nАлматы, Ауэзовский район\nhttps://go.2gis.com/i0trd"""
}

# -------------SQL TABLES
Category = """
    create table if not exists Category(
        category_id serial primary key,
        category_name varchar
    );
    """

Variation = """
    create table if not exists Variation(
        variation_id serial primary key,
        variation_name varchar,
        category_id int references Category(category_id) on delete cascade 
    );
    """

Client   = """
    create table if not exists Client(
        client_id serial primary key,
        chat_id int,
        first_name varchar,
        last_name varchar,
        username varchar,
        registered TIMESTAMPTZ DEFAULT Now()
    );
"""

Phone = """
    create table if not exists Phone(
        phone_id serial primary key,
        phone_number varchar,
        client_id int references Client(client_id) on delete cascade
    );
"""

Quiz    = """
    create table if not exists Quiz(
        quiz_id serial primary key,
        client_id int references Client(client_id) on delete cascade 
    );
"""

Client_has_Variation = """
    create table if not exists Client_has_Variation(
        chv          serial         primary key,
        quiz_id      int references Quiz    (quiz_id)       on delete cascade,
        category_id  int references Category(category_id)   on delete cascade,
        variation_id int references Variation(variation_id) on delete cascade
    );
"""

Video = """
    create table if not exists Video(
        video_id serial primary key,
        video_name varchar,
        video_url varchar
    );
"""

Video_has_Variation = """
    create table if not exists Video_has_Variation(
        vhv serial primary key,
        video_id int references Video(video_id) on delete cascade,
        variation_id int references Variation(variation_id) on delete cascade
    );
"""

query = """
select v.video_name from Video v
inner join Video_has_Variation vv
on v.video_id = vv.video_id
inner join Client_has_Variation cv on cv.variation_id = vv.variation_id
"""


qq1 = """
select variation_id from Client_has_Variation 
where quiz_id = %s and category_id = %s
"""

qq = """
select DISTINCT v.video_name from Video v,Video_has_Variation vv
where v.video_id = vv.video_id and where vv.variation_id = %s and variation_id = %s and variation_id = %s
"""


ABOUT_KZ = """
<b>
Yqylas Films - 2015 жылы құрылған фото/видео продакшн.

Осы күнге дейін 300 ден астам Love Story,
260 тан астам мерекелік кештер, 10 нан астам бейнебаян, 100 ден астам жарнамалық роликтер түсірдік.

Бізге әр тұтынушымыздың идеясы және ойы маңызды. Себебі бұл сіздердің өмірлік сақталатын фото/видео болған соң, барынша сапаға әрі сервиске жұмыс жасау маңызды деп білеміз. 

Толыққанды ақпарат алу үшін біздің инстаграм парақшаға өтіңіз:

www.instagram.com/yqylasfilms

Немесе біздің офисқа келіп, өз махаббат оқиғаңыздың сценарийін тегін жаздыра аласыздар. 🤗

Алматы қаласы; мкр Қуаныш 17
( ориентир Жандосов Сайн )

Телефон нөмеріңізді жіберіңіз. Және біз жауаптарыңызға байланысты сізге тегін консультация жүргізетін боламыз. 🤗

Yqylas Films - 2015 жылы құрылған фото/видео продакшн.

Осы күнге дейін 300 ден астам Love Story,
260 тан астам мерекелік кештер, 10 нан астам бейнебаян, 100 ден астам жарнамалық роликтер түсірдік.

Бізге әр тұтынушымыздың идеясы және ойы маңызды. Себебі бұл сіздердің өмірлік сақталатын фото/видео болған соң, барынша сапаға әрі сервиске жұмыс жасау маңызды деп білеміз. 

Толыққанды ақпарат алу үшін біздің инстаграм парақшаға өтіңіз:

www.instagram.com/yqylasfilms

Немесе біздің офисқа келіп, өз махаббат оқиғаңыздың сценарийін тегін жаздыра аласыздар. 🤗

Алматы қаласы; мкр Қуаныш 17
( ориентир Жандосов Сайн )
</b>
"""

ABOUT_RU = """
<b>
Yqylas Films - фото/видео продакшн,который запустил свою работу в 2015 году.

До этого времени мы сняли более чем 300 Love Story, 260 мероприятий ,10+ клипов и больше чем 100 рекламных роликов.

Нам важно что думаете Вы. Потому что это работа которая остаётся на всю жизнь,а мы в свою очередь стараемся работать на качество и на сервис. 🤗

Чтобы взять полную информацию пройдите в наш инстаграм:

www.instagram.com/yqylasfilms

Или вы можете приехать в наш офис и мы для Вас напишем бесплатный сценарий про вашу историю любви. 💝

Город Алматы: мкр Куаныш 17
(Ориентир на  Жандосова Сайна)
</b>
"""

ABOUT_US = {
    True : ABOUT_KZ,
    False : ABOUT_RU
}