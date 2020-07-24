
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

INTERFACE_LANGUAGE = {'🇰🇿Қазақ тілі' : True,'🇷🇺Русский язык' : False}

WELCOME_LANGUAGE = {
        True  : ['Біз жайлы🎥','Квиз өту🎯','Жұмыстар🎬','Контактілер📞', 'Мекен-жай🏢', 'Прайслист🗒','🇰🇿 🔁 🇷🇺','Кездесуге жазылу👥'],
        False : ['Про нас🎥','Пройти квиз🎯', 'Работы🎬', 'Контакты📞', 'Адресс🏢', 'Прайслист🗒', '🇰🇿 🔁 🇷🇺','Записаться на встречу👥']
}

PRICE_LIST_TYPE = {
    True  : ['ТОЙ', 'LOVESTORY'],
    False : ['СВАДЬБА', 'LOVESTORY']
}

LOVESTORY_PACKET = ['Classic', 'Premium', 'Exclusive']
WEDDING_PACKET   = ['Standart', 'Silver', 'Gold']


PRICE_LIST = {
    True : {
        PRICE_LIST_TYPE[True][0] : ['']
    }
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

Quiz    = """
    create table if not exists Quiz(
        quiz_id serial primary key,
        client_id int references Client(client_id) on delete cascade 
    );
"""

Client_has_Variation = """
    create table if not exists Client_has_Variation(
        chv serial primary key,
        quiz_id int references Quiz(quiz_id) on delete cascade,
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



    
