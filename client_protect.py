import socket
from crypt_func import *

def get_key_client():
    with open('key_client.txt', 'r') as txt:
        for row in txt:
            return row

sock = socket.socket()

sock.connect(('localhost', 9090))
print("Установка соединения с сервером")

keys = dict(map(lambda x: x.split(':'), get_key_client().split(', ')))
g, p, a = int(keys['g']), int(keys['p']), int(keys['a'])
A = client_key_send(a, g, p)
dec_msg = str(g) + " " + str(p) + " " + str(A)
msg = vernam(dec_msg)
sock.send(msg.encode())
print("Отправка данных")
K = ""
print("Начало приёма данных от сервера")
data = sock.recv(1024)
K = client_receive(int(data.decode()), a, p)
print("KEY:", K)
print("Сообщение от сервера: ", data.decode())
print("Конец приёма данных от сервера")

sock.close()
print("Разрыв соединения с сервером")
