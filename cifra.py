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

def createPairs(text):



pathInput = input('Digite o caminho do arquivo de entrada: ')
contentInput = readFile(pathInput)
if contentInput == None:
    exit()

key = input('Digite a key: ')
key = formatKey(key)
if key == None:
    exit()

table = createTable(key)

acao = input('Digite C para cifrar e D para decifrar: ').upper()
if acao == 'C':
    pass
elif acao == 'D':
    pass
else:
    print('Opção inválida.')



# arquivoOutput = input('Digite o caminho do arquivo de saída: ')
