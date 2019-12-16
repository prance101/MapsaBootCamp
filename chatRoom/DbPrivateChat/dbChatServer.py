import psycopg2 ; import socket
import time     ; import select
from Singleton import A
from dbUsers import *

i = 0  ; j = 0 ; friend_list = []

#IP = '172.30.18.90'
IP = "localhost"
PORT = 8210

header_lenght = 10

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen(10)
print("Server Run!")

socket_list = [server_socket]
clients = {} ; clients_name = {}

sngton = A()

while True:
    try:
        read_socket, write_socket, exception_socket = select.select(
            socket_list, [], socket_list)
        print("read_socket", read_socket)
        for s in read_socket:
            if s == server_socket:
                client_socket, address = server_socket.accept()

                if client_socket:
                    client_socket.send(bytes("welcome!", 'utf-8'))
                    socket_list.append(client_socket)
                    user = address[0]
                    clients[client_socket] = user
                    print("Connection Established from {}".format(address))
                    for client_sockets in clients:
                        if client_sockets != client_socket:
                            client_sockets.send(
                                bytes("{} joined Group!".format(address), 'utf-8'))


            else:

                # moshakhas bodan vaziate Friend
                if i == 0:
                    message = s.recv(1024)
                    input_msg = message.decode('utf-8')
                    friend_list.append(input_msg)
                    if input_msg not in online_list and input_msg not in busy_list:
                        client_sockets.send(bytes("Your friend is Online", 'utf-8'))
                        i = 1  ;  j = 1
                    elif input_msg in online_list:
                        client_sockets.send(bytes("Your friend is Offline", 'utf-8'))
                    elif input_msg in busy_list:
                        client_sockets.send(bytes("Your friend is Busy"   , 'utf-8'))
                    else:
                        client_sockets.send(bytes("Your friend Not Register", 'utf-8'))

                else:
                    # agar friend on shavad chat 2 nafare
                    if j == 1:
                        message = s.recv(1024)
                        input_msg = message.decode('utf-8')

                        split_msg = input_msg.split("-")
                        sngton.name = split_msg[0]
                        clients_name[client_socket] = split_msg[0]

                        if not message:
                            socket_list.remove(s)
                            del clients[s]
                            continue

                        for client_socket in clients:
                            if client_socket != s:
                                client_socket.send(message)

        for s in exception_socket:
            socket_list.remove(s)
            del clients[s]
        print("socket list \n", socket_list)

    except:
        continue