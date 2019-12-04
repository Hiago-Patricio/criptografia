import string


'''
Faz a leitura do arquivo e formata o texto lido
'''
def readFile(pathInput):
    try:
        with open(pathInput, 'r') as f:
            textInput = f.read()
        textInput = textInput.replace(' ','')
        textInput = textInput.upper()
        textInput = textInput.replace('Y', '')
        return textInput
    except:
        print('Caminho inválido.')
        return None


def writeFile(path, text):
    try:
        with open(path, 'w+') as f:
            f.write(text)
        return True
    except:
        return False

def formatKey(key):
    key = key.replace(' ', '')
    key = key.upper()
    key = ''.join(sorted(set(key), key = key.index))
    key = key.replace('Y', '')
    if key == '':
        print('Chave inválida.')
        return None
    return key


'''
Lê a key e devolve uma table 5x5 em uppercase
'''
def createTable(key):
    alphabet = string.ascii_uppercase
    alphabet = key + alphabet
    alphabet = alphabet.replace('Y', '')
    alphabet = ''.join(sorted(set(alphabet), key=alphabet.index))
    table = [[] for i in range(5)]
    for i in range(5):
        for j in range(5):
            letra = alphabet[i*5 + j]
            table[i].append(letra)
    return table


def createPairsToEncrypt(text):
    text = list(text)
    prepareText = ''
    posLeft = 0
    posRight = 1
    # insere os X's necessários
    while True:
        lastPosition = len(text) - 1

        if posLeft < lastPosition and posRight <= lastPosition:
            if text[posLeft] != text[posRight]:
                prepareText += text[posLeft] + text[posRight] 
                posLeft += 2
                posRight += 2
            else:
                prepareText += text[posLeft] + 'X'
                posLeft += 1
                posRight += 1
        elif posLeft == lastPosition:
            prepareText += text[posLeft] + 'X'
            break
        elif posLeft > lastPosition:
            break

    pairs = [prepareText[i:i+2] for i in range(0, len(prepareText), 2)]
    print(pairs)
    return pairs


def createPairsToDecipher(text):
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    return pairs


def findLetterPositionInTable(letter, table):
    for i in range(5):
        for j in range(5):
            if letter == table[i][j]:
                return i, j


def encrypt(textInput, table):
    textEncrypted = ''
    pairs = createPairsToEncrypt(textInput)

    for pair in pairs:
        row1, col1 = findLetterPositionInTable(pair[0], table) 
        row2, col2 = findLetterPositionInTable(pair[1], table) 
        
        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1
        
        textEncrypted += table[row1][col1]
        textEncrypted += table[row2][col2]

    return textEncrypted


def decipher(textInput, table):
    textDeciphered = ''
    pairs = createPairsToDecipher(textInput)

    for pair in pairs:
        row1, col1 = findLetterPositionInTable(pair[0], table) 
        row2, col2 = findLetterPositionInTable(pair[1], table) 
        
        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            col1, col2 = col2, col1
        
        textDeciphered += table[row1][col1]
        textDeciphered += table[row2][col2]

    return textDeciphered


pathInput = input('Digite o caminho do arquivo de entrada:\n')
contentInput = readFile(pathInput)
if contentInput == None:
    exit()

key = input('Digite a key:\n')
key = formatKey(key)
if key == None:
    exit()

table = createTable(key)
for i in table:
    print(i)

acao = input('Digite C para cifrar e D para decifrar:\n').upper()
if acao == 'C':
    textOutput = encrypt(contentInput, table)
elif acao == 'D':
    textOutput = decipher(contentInput, table)
else:
    print('Opção inválida.')

fileOutput = input('Digite o caminho do arquivo de saída:\n')
if writeFile(fileOutput, textOutput):
    print('Arquivo salvo com sucesso.')
else:
    print('Falha em salvar o arquivo.')