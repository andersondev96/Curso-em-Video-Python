"""

Faça um programa que leia um ângulo qualquer e mostre na 
tela o valor do seno, cosseno e a tangente desse ângulo.

"""
from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} graus têm: '.format(angulo))
print('Seno: {:.2f} ' .format(seno))
print('Cosseno: {:.2f}' .format(cosseno))
print('Tangente: {:.2f}' .format(tangente))
