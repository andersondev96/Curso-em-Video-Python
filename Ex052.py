""""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
num = int(input('Digite um numero: '))
cont = 0
for c in range(num, 0, -1):

    if num % c == 0:
        print('\033[1;33m{}\033[m'.format(c), end=' ')
        cont += 1
    else:
        print('\033[1;31m{}\033[m'.format(c), end=' ')
print()
print('O numero {} foi divisível {} vezes'.format(num, cont))
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
