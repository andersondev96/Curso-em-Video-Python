"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import  itemgetter
jogo = dict()
jogo = {'jogador1': randint(1, 6), 'jogador2': randint(0, 6), 'jogador3': randint(0, 6), 'jogador4': randint(0, 6)}
ranking = list()
print('valores sorteados:')
for k, v in jogo.items():
    sleep(0.5)
    print(f'O {k} tirou {v} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('== RANCKING DOS JOGADORES ==' )
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
