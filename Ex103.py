"""
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou. O programa deverá ser capaz de
mostrar a ficha do jogador, mesmo que algum dado não tenha
sido informado
"""

def ficha(nome='<desconhecido>', gols=0):
    print( f'O jogador {nome} fez {gols} gol(s) no campeonato')


# Programa principal
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome,gols)
