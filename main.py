from math import ceil
import secrets
from re import findall

def encode(string):

    # Váriavel para estocar a string encriptada
    encrypt_string = ''

    # Para cada letra na string inicial, a string encriptada vai ter a letra uma posição a menos,
    # ou seja, se a posição da letra é 10, será 9
    # Após isso é somado a posição metade da quantidade de caracteres arredondado para cima
    for x in range(len(string)):
        if len(string) < 2:
            print('Insira uma palavra, não uma letra.')
        else:
            encrypt_string += string[-x + ceil(len(string)/2)] 


    array = []
    vogais = 'AEIOU'

    for x in range(len(vogais)):
        array.append(secrets.token_hex(3))

    # Aqui estamos substituindo as vogais para outros valores

    for x in range(len(vogais)):
        encrypt_string = encrypt_string.replace(vogais[x],array[x])

    hash_code = ''

    for x in range(len(array)):
        hash_code += array[x]

    return f'Seu código secreto é "{hash_code}", guarde-o para descriptografar. Sua palavra encriptada é "{encrypt_string}" '

def decode(string, hash):
    # Aqui recebemos a string e substituímos os valores modificados para as vogais novamente

    vogais = 'AEIOU'
    code = findall('......', hash)

    for x in range(len(vogais)):
        string = string.replace(code[x], vogais[x])

    # Váriavel para estocar a string descriptografada
    final_string =''

    # O mesmo processo de encriptação faz ele decodificar
    for x in range(len(string)):
        final_string += string[-x + ceil(len(string)/2)]

    return f'A palavra decodificada é "{final_string}"'

# Menu

def menu():

    print('''
        
        _               _           __ 
        | |             (_)         /_ |
        | |__   __ _ ___ _  _____   _| |
        | '_ \ / _` / __| |/ __\ \ / / |
        | |_) | (_| \__ \ | (__ \ V /| |
        |_.__/ \__,_|___/_|\___| \_/ |_|
                                 
                                 
    Olá, esse é o criptografador Basicv1, o que deseja fazer?
    [1] - 🔒 Criptografar
    [2] - 🔑 Descriptografar

    ''')

    option = input('👉 Qual sua escolha? ')

    if option == '1':
        string = input("Digite o texto que deseja criptografar: ")
        print(encode(string.upper()))
    elif option == '2':
        string = input("Digite o texto criptografado que deseja descriptografar: ")
        code = input("Insira o código secreto: ")
        print(decode(string, code))
    else:
        print('⚠ OPÇÃO INVÁLIDA!!!')
        menu()

menu()
