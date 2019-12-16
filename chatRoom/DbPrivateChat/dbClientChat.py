import socket ; import time ; import sys ; import threading ;
from dbUsers import *  ;  from dbChat import *
import re
from Singleton import *

i =0
sngton = A()

#IP   = '172.30.18.90'
IP   = "localhost"
PORT = 8210

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(0)

login = input("input Username : ")

# agar username karbar dar dakhel database bashad ba username varde mishavad
if str(login) in usersname_list:
    print("Loging")
    sngton.username = str(login)

    update_query = """Update users set ONLINE = %s where USERNAME = %s"""
    cursor.execute(update_query, (True, (login)))

# agar username karbar dar dakhel database na bashad bayad Register namayad
else:
    print("Registration: ")
    Client_details = input(
        "Enter your Details:\n Sample:username-age-True(male) or False(woman)-USA \n >> ")

    #split kardane etelate karbar baraie varde kardan be Database
    split_msg = Client_details.split("-")

    # SINGLETON
    sngton.username = split_msg[0]

    # rgx1 = re.split_msg[0]


    sngton.age  = int(split_msg[1])
    sngton.gender  = split_msg[2]
    sngton.country = split_msg[3]

    print("Username: "+split_msg[0]+"  .Age: "+split_msg[1]+"  .Male:"+split_msg[2]+"  .Country: "+split_msg[3])


    #moshakase nemodane halate True va False barie jensiate karbar
    if split_msg[2] == 'True':
        man = True
    else:
        man = False

    #vared kardane etelate karbar dar Database
    records = (split_msg[0], int(split_msg[1]), man, split_msg[3],None,None)
    result = cursor.execute(insert_query, records)

    #update kardan halate ONLINE bodan
    update_query = """Update users set ONLINE = %s where USERNAME = %s"""
    cursor.execute(update_query, (True, sngton.username))


# vared kardan name Friend
friend_name = input("Enter your friend Username: ")
client_socket.send(bytes(friend_name,'utf-8'))

def send_message():
    while True:
        msg = input()

        # Busy
        if i == 0 :
            update_query = """Update users set BUSY = %s where USERNAME = %s"""
            cursor.execute(update_query, (True, sngton.username))
            connection.commit()


        # ezafe kardan Eixt baraie khoroj :  exit()
        if str(msg) == "exit()":
            update_query = """Update users set ONLINE = %s where USERNAME = %s"""
            cursor.execute(update_query, (False, sngton.username))
            connection.commit()
            cursor.close()
            print("Connection Closed!")
            sys.exit()


        client_socket.send(bytes(sngton.username + ">> " + msg, 'utf-8'))


        #update_qry = """Update users set CHATLIST = %s"""
        #cursor.execute(update_qry, str(msg))
        #connection.commit()

t1 = threading.Thread(target=send_message)
t1.start()

while True:

    try:
        while True:
            message = client_socket.recv(1024)

            if not message :

                # update kardan OFFLINE be database
                update_query = """Update users set ONLINE = %s where USERNAME = %s"""
                cursor.execute(update_query, (False, sngton.username))

                connection.commit()
                cursor.close()
                print("Connection Closed!")
                sys.exit()
            print(message.decode('utf-8'))

    except IOError as e:
        pass

    time.sleep(1)
