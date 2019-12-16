import psycopg2

online_list = []  ;  busy_list = []  ;  usersname_list = []

connection = psycopg2.connect(user = "postgres",
                                password = "postgres",
                                host = "127.0.0.1",
                                port = "5432",
                                database = "members")

cursor = connection.cursor()

create_table = '''CREATE TABLE members
    (PID  SERIAL   PRIMARY KEY   NOT NULL,
    BOOKNAME       VARCHAR(250)  NOT NULL,
    BOOKCOUNT      INT                   ,
    NUMBORROWED    INT          NOT NULL); '''

#cursor.execute(create_table)

insert_query = """ INSERT INTO members (BOOKNAME, BOOKCOUNT, NUMBORROWED) 
                        VALUES (%s,%s,%s) """

Books = [('Atomic Habits', 2, 0) , ('To Kill a Mockingbird', 2, 1) , ('The Harry Potter', 5, 2),
           ('The Little Prince', 5, 1) , ('The Lord of the Rings', 6, 3) , ('Siddhartha', 1, 0),
           ('The Count of Monte Cristo', 4, 2) , ('Candide', 2, 0) , ('Game of Thrones', 6, 5),
           ('The Alchemist', 3, 1)]

#result = cursor.executemany(insert_query, Books)

#connection.commit()
#count = cursor.rowcount
#print (count, "Record inserted successfully into mobile table")
# Query = "select * from users"
# cursor.execute(Query)
# users_records = cursor.fetchall()



connection.commit()
#cursor.close()