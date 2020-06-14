"""
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
"""
from time import sleep


def linha():
    print('-=' * 20)


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        p = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            sleep(1)
            print(f'{c}', end=' ')
        print('FIM!')
    else:
        for c in range(inicio, fim-1, -passo):
            sleep(1)
            print(f'{c}', end=' ')
        print('FIM!')
    linha()



linha()
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
linha()
contador(inicio, fim, passo)

