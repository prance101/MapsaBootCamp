import socket
import time
import select

#IP = '172.30.18.90'
IP = "localhost"
PORT = 8210

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(10)
print("Server Run!")

socket_list = [server_socket]
clients = {} ; clients_name = {}
i = 0 ; j = 0 ; k = 0 ; host = [] ; gest = []

while True:
    read_socket, write_socket, exception_socket = select.select(
        socket_list, [], socket_list)
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
                        k = 1
                        client_sockets.send(
                            bytes("{} joined Group!".format(address), 'utf-8'))

        else:
            print(clients_name)
            if i == 0:
                if j == 0:
                    message = s.recv(1024)
                    encode_message = message.decode('utf-8')
                    host.append(message.decode('utf-8'))
                    clients_name[client_socket] = encode_message
                    client_socket.send(bytes("\nPlZ wait...\n", "utf-8"))
                    j = 1

                elif j == 1:
                    message = s.recv(1024)
                    encode_message = message.decode('utf-8')
                    gest.append(message.decode('utf-8'))
                    gest.append(host[0])
                    host.pop()
                    j = 2

                if k == 1:
                    message = s.recv(1024)
                    encode_message = message.decode('utf-8')
                    if encode_message in gest:
                        socket_list[1].send(bytes("\nYour friend is online\n", "utf-8"))
                        client_socket.send(bytes("\nYou are in private chat\n", "utf-8"))
                        i = 2
                    else:
                        socket_list.remove(s)
                        del clients[s]

            if i == 2:
                message = s.recv(1024)
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
    # print(socket_list)
# server_socket.close()
