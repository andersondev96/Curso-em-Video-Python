"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só
será interrompido quando o jogador perder, mostrando o total de
vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

v = 0
soma = 0
print('=-' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 10)
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma}', end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!!!')
            v += 1
        else:
            print('Você PERDEU!!!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!!!')
            v += 1
        else:
            print('Você PERDEU!!!')
            break;
    print('Vamos jogar novamente ...')
print(f'GAME OVER! Você venceu {v} vezes.')
