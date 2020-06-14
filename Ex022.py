"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiusculas e minusculas
Quantas letras ao todo sem considerar espaços.
Quantas letras tem o primeiro nome.
"""
nome = str(input('Digite seu nome: ')).strip()
print('Analisando o seu nome ...')
print('O seu nome em maiusculas é {}.'.format(nome.upper()))
print('O seu nome em minusculas é {}.'.format(nome.lower()))
print('O seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome e {} e ele tem {} letras'.format(separa[0], len(separa[0])))
