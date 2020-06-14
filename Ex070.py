"""
 Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
total = maisde1000 = maisbarato = cont = 0
barato = ''
print('-' * 30)
print('       LOJA SUPER BARATAO')
print('-' * 30)

while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        maisde1000 += 1
    if cont == 1 or preco < maisbarato:
        maisbarato = preco
        barato = nome
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar ? [S/N] ')).upper().split()[0]
    if op == 'N':
        break

print('{:-^40}' .format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisde1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${maisbarato:.2f}')

