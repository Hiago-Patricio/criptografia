import string
import re

def read_file(path):
    try:
        with open(path, 'r') as f:
            text = f.read()
        return text
    except:
        pass


def write_file(path, text):
    try:
        with open(path, 'w+') as f:
            f.write(text)
        return True
    except:
        return False


def format_text(text):
    text = text.upper()
    text = re.sub('[^A-Z]+', '', text).replace('Y', '')
    return text


def format_key(key_crypt):
    key_crypt = format_text(key_crypt)
    key_crypt = ''.join(sorted(set(key_crypt), key = key_crypt.index))
    return key_crypt


def create_playfair_cipher(key):
    alphabet = string.ascii_uppercase
    alphabet = alphabet.replace('Y', '')
    for letter in key:
        alphabet = alphabet.replace(letter, '')
    alphabet = list(alphabet)

    matrix_playfair = []
    [matrix_playfair.append([]) for i in range(5)]

    for aux in range(len(key)):
        i = int(aux / 5)
        matrix_playfair[i].append(key[aux])

    j = 0
    for aux in range(len(key), 25):
        i = int(aux / 5)
        matrix_playfair[i].append(alphabet[j])
        j += 1

    return matrix_playfair


def create_pairs(text):
    text = list(text)
    pairs = []

    i = 0
    while i < len(text):
        if(i + 1 < len(text) and text[i] != text[i+1]):
            pairs.append(text[i] + text[i+1])
            i += 2        
        else:
            pairs.append(text[i] + 'X')
            i += 1
    return pairs


def find_position_playfair_cipher(letter, matrix_playfair):
    for i in range(5):
        for j in range(5):
            if letter == matrix_playfair[i][j]:
                return i, j



def encrypt(text, key):
    matrix_playfair = create_playfair_cipher(key)
    pairs_clean = create_pairs(text)
    text_encryted = ''

    for pair in pairs_clean:
        row1, col1 = find_position_playfair_cipher(pair[0], matrix_playfair) 
        row2, col2 = find_position_playfair_cipher(pair[1], matrix_playfair) 
        
        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1
        
        text_encryted += matrix_playfair[row1][col1]
        text_encryted += matrix_playfair[row2][col2]

    return text_encryted


def decrypt(text, key):
    matrix_playfair = create_playfair_cipher(key)
    pairs_clean = create_pairs(text)
    text_encryted = ''

    for pair in pairs_clean:
        row1, col1 = find_position_playfair_cipher(pair[0], matrix_playfair) 
        row2, col2 = find_position_playfair_cipher(pair[1], matrix_playfair) 
        
        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            col1, col2 = col2, col1
        
        text_encryted += matrix_playfair[row1][col1]
        text_encryted += matrix_playfair[row2][col2]

    return text_encryted


def read_input():
    while True:
        path = input('Digite o path do arquivo de entrada: ')
        text = read_file(path)
        if text != None:
            break
        print('Caminho inválido.')

    while True:
        key = input('Digite a chave de criptografia: ')
        key = format_key(key)
        if key != '':
            break
        print('Chave inválida.')

    while True:
        option = input('Digite D para decriptar e E para encriptar').upper()
        if option == 'E':
            text = encrypt(text, key)
            break
        elif option == 'D':
            pass
            text = decrypt(text, key)
            break
        print('Opção inválida.')

    while True:
        path = input('Digite o path do arquivo de saída: ')
        if write_file(path, text) == True:
            break
        print('Caminho inválido.')


read_input()