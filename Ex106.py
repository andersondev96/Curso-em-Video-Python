"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
Importante: use cores.
"""

from time import  sleep

c = ('\033[m',
    '\033[0;30;41m',
    '\033[0;30;42m',
    '\033[0;30;43m',
    '\033[0;30;44m',
    '\033[0;30;45m',
    '\033[7;30m'
     )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(c[0], end='')
    sleep(1)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA pyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)


titulo('ATÉ LOGO', 1)
