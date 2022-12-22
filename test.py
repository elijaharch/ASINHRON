def get_key_client():
    with open('key_client.txt', 'r') as txt:
        for row in txt:
            return row

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




#print(dict(map(lambda x: x.split(':'), get_key_client().split(', '))))