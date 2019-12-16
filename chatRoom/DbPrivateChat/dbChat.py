import psycopg2

connection = psycopg2.connect(user = "postgres",
                                password = "postgres",
                                host = "127.0.0.1",
                                port = "5432",
                                database = "Chatroom")

#cursor = connection.cursor()

create_table = '''CREATE TABLE Chat
    (ID  SERIAL PRIMARY KEY     NOT NULL,
    NAME       VARCHAR(50)      NOT NULL,
    CHATLIST   VARCHAR(255)        ; '''

#cursor.execute(create_table)

insert_qry = """ INSERT INTO users (NAME, CHATLIST) 
                        VALUES (%s,%s) """

connection.commit()
#print("Success")
#cursor.close()