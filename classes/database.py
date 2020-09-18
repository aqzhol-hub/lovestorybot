from psycopg2 import connect

query = """
select DISTINCT v.video_name from Video v
inner join Video_has_Variation vv
on v.video_id = vv.video_id
inner join Client_has_Variation cv on cv.variation_id = vv.variation_id
where cv.quiz_id = %s
"""




lis = [
    [23,[5,7,14]],
    [22,[4,9,13,14]],
    [21,[4,8,13]],
    [20,[5,8,14]],
    [19,[6,7,13,14]],
    [17,[5,7,14]],
    [16,[6,8,14]],
    [15,[5,7,14]],
    [14,[5,8,14]],
    [13,[4,9,14,13]],
    [12,[6,9,14,15]],
    [11,[4,8,13]],
    [10,[4,5,8,9,13,15]],
    [9,[5,7,14]],
    [8,[4,8,13,14]],
    [7,[5,9,13,14]],
    [6,[5,9,15]],
    [5,[6,7,14,13]],
    [3,[4,8,13]],
    [2,[4,8,14,13]],
    [1,[6,8,14]]
]

#style 456
#form 789
#location 13 14 15

# ['classic',  'dynamic',  'extremely'],   # style
# ['ethno',    'classica', 'arthouse' ],   # form
# ['city',     'nature',   'studio'   ],   # location



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


# dbname = 'puttgvir'
# user = 'puttgvir'
# password = 'scuWJvr8CgsuGpkzgyC3YBsHVdz7cbED'
# host = 'rogue.db.elephantsql.com'
# port = '5432'

# connection = connect(dbname=dbname,user=user,password=password,host=host,port=port)
# cursor = connection.cursor()




class Database():


    # --------Constructor
    def __init__(self,dbname,user,password,host,port):

        self.connection = connect(dbname = dbname, user = user, password = password, host = host, port = port)
        self.cursor = self.connection.cursor()


    def into(self):
        for i in lis:
            for j in i[1]:
                try:
                    with self.connection:
                        self.cursor.execute("insert into Video_has_Variation(video_id,variation_id) values(%s,%s)",(i[0],j))
                        self.connection.commit()
                    print(i[0],j)
                except Exception as e:
                    print(e)
                
        


    def fet(self,quiz_id):

        li = [2,3,5]
        tup = tuple()
        for i in li:
            try:
                with self.connection:
                    self.cursor.execute("select variation_id from Client_has_Variation where quiz_id = %s and category_id = %s",(quiz_id,i))
                    tup += (self.cursor.fetchall()[-1][0],)
            except Exception as e:
                print(e)
        return tup

    def get(self,chat_id):

        qq = """
        select DISTINCT v.video_name,v.video_url from Video v,Video_has_Variation vv
        where v.video_id = vv.video_id and vv.variation_id in (%s,%s,%s)
        """
        #ls.jpeg
        varis = self.fet(self.__quiz_id(chat_id))
        retur = ''
        try:
            with self.connection:
                self.cursor.execute(qq,(varis[0],varis[1],varis[2]))
                retur =   self.cursor.fetchall()[-3:]
        except Exception as e:
            print(e)

        result = ""
        for i in retur:
            result += """\n<a href="{1}">{0}</a>\n""".format(i[0],i[1])
        return result

        
    
    # --------Public methods
    def add_client(self,chat_id,first_name,last_name,username):

        try:
            with self.connection:
                self.cursor.execute("insert into Client(chat_id,first_name,last_name,username) values(%s,%s,%s,%s) on conflict do nothing", (chat_id,first_name,last_name,username))
                self.connection.commit()
        except Exception as e:
            print(e)

    def add_client_liking(self,chat_id,variation_name):

        try:
            with self.connection:
                self.cursor.execute("insert into Client_has_Variation(quiz_id,category_id,variation_id) values(%s,%s,%s)", (self.__quiz_id(chat_id),self.__category_id(variation_name),self.__variation_id(variation_name)))
                self.connection.commit()
        except Exception as e:
            print(e)

    def add_quiz(self,chat_id):

        try:
            with self.connection:
                self.cursor.execute("insert into Quiz(client_id) values (%s)",[self.__client_id(chat_id)])
                self.connection.commit()
        except Exception as e:
            print(e)

    def add_contact(self,phone_number,chat_id):

        try:
            with self.connection:
                self.cursor.execute("insert into Phone(phone_number,client_id) values(%s, %s)", (phone_number,self.__client_id(chat_id)))
                self.connection.commit()
        except Exception as e:
            print(e)

   

    def quiz_result(self,chat_id):

        user_info  = self.__user_info(chat_id)
        phone_number = self.__phone_number(chat_id)

        result = "{0} {1} @{2}\n{3}/{4}/{5}🗓 {6}📞\n".format(
            user_info[0],user_info[1],user_info[2],
            user_info[3].day,user_info[3].month,user_info[3].year,
            phone_number
        )
        quiz_id = self.__quiz_id(chat_id)
        for i,j in enumerate(CATEGORIES):
            result += "<b>{0} сұрақ : {1}</b>\n".format(i+1,(CHOICES[self.__variation_name(quiz_id,j)]))
            
        return result

    def result_client(self,chat_id):
        return 'static/img/ls.jpg',self.get(chat_id)

    def get_works(self):
        
        try:
            with self.connection:
                self.cursor.execute("select video_name, video_url from Video")
                result = self.cursor.fetchall()
            from random import sample
            result = sample(result,5)

            data = ""
            for i in result:
                data += """\n<a href="{1}">{0}</a>\n""".format(i[0],i[1])
            return data
        except Exception as e:
            print(e)
        
        

        
    
        

    # --------Private methods

    def __user_info(self,chat_id):

        try:
            with self.connection:
                self.cursor.execute("select first_name,last_name,username,registered from Client where client_id = %s", [self.__client_id(chat_id)])
                return self.cursor.fetchall()[0]
        except Exception as e:
            print(e)

    
    def __phone_number(self,chat_id):

        try:
            with self.connection:
                self.cursor.execute("select phone_number from Phone where client_id = %s", [self.__client_id(chat_id)])
                return self.cursor.fetchall()[0][0]
        except Exception as e:
            print(e)

    def __variation_name(self,quiz_id,category_name):

        try:
            with self.connection:
                query = """
                select 
                v.variation_name from Variation v, Category c, Client_has_Variation cv
                where c.category_name = %s and cv.quiz_id = %s 
                and cv.category_id = c.category_id and cv.variation_id = v.variation_id
                """
                self.cursor.execute(query,(category_name,quiz_id))
                return self.cursor.fetchall()[-1][0]
        except Exception as e:
            print(e)


    def __variation_id_(self,quiz_id,category_name):

        try:
            with self.connection:
                query = """
                select 
                v.variation_id from Variation v, Category c, Client_has_Variation cv
                where c.category_name = %s and cv.quiz_id = %s 
                and cv.category_id = c.category_id and cv.variation_id = v.variation_id
                """
                self.cursor.execute(query,(category_name,quiz_id))
                return self.cursor.fetchall()[-1][0]
        except Exception as e:
            print(e)
        
        

    def __variation_id(self,variation_name):
        
        try:
            with self.connection:
                self.cursor.execute("select variation_id from Variation where variation_name = %s", [variation_name])
                return self.cursor.fetchall()[0][0]
        except Exception as e:
            print(e)
        

    def __quiz_id(self,chat_id):

        try:
            with self.connection:
                self.cursor.execute("select max(quiz_id) from Quiz where client_id = %s",[self.__client_id(chat_id)])
                return self.cursor.fetchall()[0][0]
        except Exception as e:
            print(e)

    
    def __category_id_(self,category_name):

        try:
            with self.connection:
                self.cursor.execute("select category_id from Category where category_name = %s", [category_name])
                return self.cursor.fetchall()[0][0]
        except Exception as e:
            print(e)
        

    def __category_id(self, variation_name):

        try:
            with self.connection:
                self.cursor.execute("select category_id from Variation where variation_name = %s", [variation_name])
                return self.cursor.fetchall()[0][0]
        except Exception as e:
            print(e)

        
    def __client_id(self, chat_id):

        try:
            with self.connection:
                self.cursor.execute("select client_id from Client where chat_id = %s", [chat_id])
                return self.cursor.fetchall()[0][0]
        except Exception as e:
            print(e)

    def __category_name(self,variation_name):

        values = list(variations.values())
        keys = list(variations.keys())
        return keys[values.index([i for i in values if variation_name in i][0])]

# d = Database(dbname,user,password,host,port)




