import socket ; import time ; import sys ; import threading

#IP   = '172.30.18.90'
IP   = "localhost"
PORT = 8210

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(0)

username = input("Enter your name: ")
client_socket.send(bytes(username,'utf-8'))
friend   = input("Enter friend name: ")
client_socket.send(bytes(friend,'utf-8'))



def send_message():
    while True:
        msg = input()
        client_socket.send(bytes(username + ">> " + msg, 'utf-8'))


t1 = threading.Thread(target=send_message)
t1.start()


while True:

    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                print("Connection Closed!")
                sys.exit()
            print(message.decode('utf-8'))

    except IOError as e:
        pass

    time.sleep(1)
