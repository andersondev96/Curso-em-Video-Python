"""
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

lista = list()
dados = list()
tot = 0
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('peso: ')))
    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    lista.append(dados[:])
    dados.clear()
    tot = tot + 1
    cont = str(input('Deseja continuar [s/n]: '))
    if cont in 'Nn':
        break
print("-="*30)
print(f'Foram cadastradas {tot} pessoas na lista.')
print(f'O maior peso foi de {mai}Kg')
for p in lista:
    if p[1] == mai:
        print(f'[{p[0]}]')
print()
print(f'O menor peso foi de {men}Kg')
for p in lista:
    if p[1] == men:
        print(f'[{p[0]}]')
print()
