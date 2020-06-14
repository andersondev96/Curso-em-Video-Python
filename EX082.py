"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

lista1 = []
listaP = []
listaI = []

while True:
    n = (int(input('Digite um número: ')))
    lista1.append(n)
    if n % 2 == 0:
        listaP.append(n)
    elif n % 2 == 1:
        listaI.append(n)
    cont = input('Deseja continuar ? (S/N) ')
    if cont in 'Nn':
        break
print('-='*30)
print(f"A lista completa é {lista1}")
print(f"A lista de pares é {listaP}")
print(f"A lista de ímpares é {listaI}")
