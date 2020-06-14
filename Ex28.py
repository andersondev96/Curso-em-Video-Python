"""
Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o 
usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na
tela se o usuário venceu ou perdeu.

"""

from random import randrange
computador = randrange(0,5)
num = int(input('Pensei em um numero de 0 a 5, tente adivinhar: '))
if num == computador:
    print('Você acertou! O numero que pensei foi o {}' .format(computador))
else:
    print('Você errou! Eu pensei foi no numero {}' .format(computador))
