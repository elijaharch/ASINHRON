import socket
from crypt_func import *

def get_key_server():
    with open('key_server.txt', 'r') as txt:
        for row in txt:
            return row

def check_key(key):
    key_list = []
    with open('access_list.txt', 'r') as txt:
        for row in txt:
            key_list.append(row.replace('\n', ''))

        if not(str(key) in key_list):
            print('Сертификат доступа не существует')
            quit()

sock = socket.socket()

sock.bind(('', 9090))
print("Запуск сервера...")

sock.listen(1)
print("Начало прослушивания порта...")

while True:

    conn, addr = sock.accept()
    print("Подключился клиент: ", addr)

    b = int(get_key_server())

    print("Начало передачи данных...")
    data = conn.recv(1024)
    msg = data.decode()
    msg = vernam(msg)
    msg = msg.split()
    msg = list(map(int, msg))
    g = msg[0]
    p = msg[1]
    A = msg[2]
    server_rec = server_key_send_receive(b, g, p, A)
    B = server_rec[0]
    K = server_rec[1]
    check_key(K)
    print("KEY:", K)
    print("Сообщение от клиента:", msg)
    print("Конец передачи данных...")
    print("Начало отправки данных...")
    conn.send(str(B).encode())
    print("Конец отправки данных...")
    conn.close()
    print("Клиент отключился")
    print("Введите <<exit>> для выхода")
    work_case = input()
    if work_case == "exit":
        break
print("Сервер остановлен...")
