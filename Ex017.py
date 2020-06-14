'''

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
e mostre o comprimento da hipotenusa.

'''
from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = hypot(co,ca)
print('A hipotenusa do triângulo com catetos iguais a {:.2f} e {:.2f} e igual a {:.2f}' .format(co, ca, hip))
