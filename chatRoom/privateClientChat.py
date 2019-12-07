import socket ; import time ; import sys ; import threading

#IP   = '172.30.19.110'
IP   = "localhost"
PORT = 8210
username = input("Enter your name: ")
friend   = input("Enter friend name: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(0)

a = 0
client_socket.send(bytes(username,'utf-8'))
client_socket.send(bytes(friend,'utf-8'))

def send_message():
    if a==1:
        while True:
            msg = input()
            client_socket.send(bytes(username + " :> " + msg, 'utf-8'))


t1 = threading.Thread(target=send_message)
t1.start()


while True:
    # #    message = client_socket.recv(1024)
    # #    print(message.decode('utf-8'))
    # msg = input('{}-> '.format(username))
    # if msg:
    #     client_socket.send(bytes(username + "->" + msg, 'utf-8'))

    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                print("Connection Closed!")
                sys.exit()
            print(message.decode('utf-8'))

    except IOError as e:
        pass

#    time.sleep(5)
