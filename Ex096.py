"""
Faça um programa que tenha uma função chamada área(), que receba
as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno.
"""

def linha():
    print('Controle de Terrenos')
    print('-'*30)


def area(l, c):
    calculo = l * c
    print(f'A área de um terreno {l}x{c} é de {calculo}m²')


linha()
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)

