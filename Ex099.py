"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e
dizer qual deles é o maior.
"""

from time import sleep
def maior(*num):
    maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for c in num:
        sleep(1)
        print(f'{c}', end=' ')
        if c > maior:
            maior = c

    print(f'Foram informados {len(num)} valores ao todo. ')
    print(f'O maior valor informado foi {maior}.')


maior(1, 2, 3, 4, 5)
maior(5, 6, 8, 50)
maior(7, 2, 0, 13, 78, 23, 44)
maior(6)
maior()
