""""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
possibilidade da digitação de um número de tipo inválido. Aproveite e crie
também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mUsuário preferiu não digitar este número.')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Por favor digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mUsuário preferiu não digitar este número.')
            return 0
        else:
            return num


n1 = leiaInt('Digite um número: ')
n2 = leiaFloat('Digite um número real: ')
print(f'\033[1;34mO valor inteiro digitado foi {n1} e o real foi {n2}\033[m')