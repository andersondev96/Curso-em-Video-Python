"""
Escreva um programa em Python que leia um número inteiro qualquer e peça para
o usuário escolher qual será a base de conversão: 1 para binário, 2 para
octal e 3 para hexadecimal
"""
print("-="*12)
print('CONVERSÃO DE BASES')
print('-='*12)
num = int(input('Digite um número: '))
print('Escolha para qual base deseja converter: ')
print('[1] - BINÁRIO')
print('[2] - OCTAL')
print('[3] - HEXADECIMAL ')
base = int(input())
if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {} '.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')

