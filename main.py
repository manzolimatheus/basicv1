from math import ceil

def encode(string):

    # Váriavel para estocar a string encriptada
    encrypt_string = ''

    # Para cada letra na string inicial, a string encriptada vai ter a letra uma posição a menos,
    # ou seja, se a posição da letra é 10, será 9
    # Após isso é somado a posição metade da quantidade de caracteres arredondado para cima
    for x in range(len(string)):
        encrypt_string += string[-x + ceil(len(string)/2)] 

    # Aqui estamos substituindo as vogais para outros valores
    encrypt_string = encrypt_string.replace('A','31x')
    encrypt_string = encrypt_string.replace('E','05x')
    encrypt_string = encrypt_string.replace('I','20x')
    encrypt_string = encrypt_string.replace('O','04x')
    encrypt_string = encrypt_string.replace('U','06x')
    encrypt_string = encrypt_string.replace(' ','210x')

    return encrypt_string

def decode(string):
    # Aqui recebemos a string e substituímos os valores modificados para as vogais novamente
    string = string.replace('31x','A')
    string = string.replace('05x','E')
    string = string.replace('20x','I')
    string = string.replace('04x','O')
    string = string.replace('06x','U')
    string = string.replace('210x',' ')

    # Váriavel para estocar a string descriptografada
    final_string =''

    # O mesmo processo de encriptação faz ele decodificar
    for x in range(len(string)):
        final_string += string[-x + ceil(len(string)/2)]

    return final_string

# Menu

def menu():

    print('''
    
     __      ____ 
     \ \    / /_ |
      \ \  / / | |
       \ \/ /  | |
        \  /   | |
         \/    |_|
              

    Olá, esse é o criptografador V1, o que deseja fazer?
    [1] - 🔒 Criptografar
    [2] - 🔑 Descriptografar

    ''')

    option = input('👉 Qual sua escolha? ')

    if option == '1':
        string = input("Digite o texto que deseja criptografar: ")
        print(encode(string.upper()))
    elif option == '2':
        string = input("Digite o texto que deseja descriptografar: ")
        print(decode(string))
    else:
        print('⚠ OPÇÃO INVÁLIDA!!!')
        menu()

menu()
