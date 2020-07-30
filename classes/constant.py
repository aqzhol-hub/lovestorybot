
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
        False : ['Про нас🎥','Пройти квиз🎯', 'Работы🎬', 'Контакты📞', 'Адресс🏢', 'Прайслист🗒', '🇰🇿 🔁 🇷🇺','Записаться на встречу👥']
}



LOVESTORY_KEYBOARD = ['Classic 97000тг', 'Premium 197000тг', 'Exclusive 397000тг', '⬅']

PRICE_KEYBOARD = {
    LOVESTORY_KEYBOARD[0]:[
        'static/img/classic.jpg',
        """
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
        """
    ],
    LOVESTORY_KEYBOARD[1]:[
        'static/img/premium.jpg',
        """
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
1 Пилон (с дроном)
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
        """
    ],
    LOVESTORY_KEYBOARD[2]:[
        'static/img/exclusive.jpg',
        """
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
1 Пилон (с дроном)
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
Инстаграм ролик(1 мин)
Видео пригласительный (1 мин)
        """
    ]
}



# -------------CONSTANT VARIABLES
ABOUT_US = {
    True : """
    <b>
        Біз жайлы
    </b>
    """,
    False : """
    <b>
        Про нас
    </b>
    """
}

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
