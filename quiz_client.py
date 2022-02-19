from email import message
from http import client
from ipaddress import ip_address
import socket
from threading import Thread

nickname = input("Choose your nickname")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

ip_address = '127.0.0.1'
port = 5000

client.connect((ip_address,port))

print("Connected with the server...")

def receive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()
