def client_key_send(a, g, p):
    A = g**a % p
    return A

def server_key_send_receive(b, g, p, A):
    B = g**b % p
    K_b = A**b % p  # Ключ сервера
    return (B, K_b)

def client_receive(B, a, p):
    K_a = B**a % p  # Ключ клиента
    return K_a

def vernam(line):  # Шифровка кодом Вернама работает в 2 стороны
    key = '00001111'
    if len(key) != 8:
        print('Ключ меньше 8')
        quit()

    code_list = []
    for sym in line:

        bin_sym = bin(ord(sym))[2:]
        if len(bin_sym) != 8:
            bin_sym = '0' + bin_sym
            while len(bin_sym) != 8:
                bin_sym = '0' + bin_sym
        encrypt_sym = ''

        for i in range(len(key)):
            if bin_sym[i] == key[i]:
                encrypt_sym += '0'
            else:
                encrypt_sym += '1'

        code_list.append('0b'+encrypt_sym)
    sym_encrypt_list = list(map(lambda x: chr(int(x, base=2)), code_list))  # Символьная шифровка
    return ''.join(sym_encrypt_list)

print(vernam('hello world'))
print(vernam('gjcc`/x`}ck'))