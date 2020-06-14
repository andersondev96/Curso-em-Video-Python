jogador = dict()
gols = []
soma = 0

jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantos partidas {jogador["nome"]} jogou: '))
for c in range(1, tot + 1):
    gols.append(int(input(f'    Quantos gols na partida {c}: ')))

jogador['gols'] = gols
for g in gols:
    soma += g
jogador['total'] = soma

print('-='*40)
print(jogador)
print('-='*40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*40)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1}, ele fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

