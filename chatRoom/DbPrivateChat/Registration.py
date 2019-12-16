import psycopg2

online_list = []  ;  busy_list = []

connection = psycopg2.connect(user = "postgres",
                                password = "postgres",
                                host = "127.0.0.1",
                                port = "5432",
                                database = "Chatroom")

cursor = connection.cursor()

create_table = '''CREATE TABLE users
    (PID  SERIAL   PRIMARY KEY   NOT NULL,
    USERNAME       VARCHAR(50)   NOT NULL,
    AGE       INT  check(AGE>15) NOT NULL,
    GENDER    BOOL               NOT NULL,
    COUNTRY   VARCHAR(50)        NOT NULL,
    ONLINE    BOOL           default FALSE,
    bUSY      BOOL           default FALSE); '''

cursor.execute(create_table)

insert_query = """ INSERT INTO users (NAME, AGE, GENDER, COUNTRY, ONLINE, BUSY) 
                        VALUES (%s,%s,%s,%s,%s,%s) """


Query = "select * from users"
cursor.execute(Query)
users_records = cursor.fetchall()

for x in users_records:
    if str(x[5]) == "True":
        online_list.append(str(x[1]))
    else:
        continue

    if str(x[6]) == "True":
        busy_list.append(str(x[1]))
    else:
        continue

    print(x[1]+" is online: "+ str(x[5]) + " _ and Busy: "+ str(x[6]))



connection.commit()
