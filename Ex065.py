""""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior  e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores.
"""
res = 'S'
cont = 0
soma = 0
media = 0
maior = 0
menor = 0
while res in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma/cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
