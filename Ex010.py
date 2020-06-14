"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar.
Considere US$1.00 = R$4.32
"""

reais = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolares = reais / 4.32
print('Com R${:.2f} você pode comprar US${:.2f}' .format(reais, dolares))
