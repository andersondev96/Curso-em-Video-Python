"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"

"""
nome = str(input('Qual é o seu nome completo? ')).strip().lower().split()
print('Seu nome tem Silva? {}'.format('SILVA' in nome))
