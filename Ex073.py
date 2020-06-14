"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""
times = ('Flamengo','Santos','Palmeiras','Grêmio','Athletico-PR',
'São Paulo','Internacional','Corinthians','Fortaleza',
'Goiás','Bahia','Vasco da Gama','Atlético-MG','Fluminense',
'Botafogo','Ceará','Cruzeiro','CSA','Chapecoense','Avaí')
print('-='*20)
print(f'Lista de times do Brasileirão: {times}')
print('-='*20)
print(f'Os 5 primeiro times são: {times[:5]}')
print('-='*20)
print(f'Os 4 últimos times são: {times[-4:]}')
print('-='*20)
print(f'Times na ordem alfabética: {sorted(times)}')
print('-='*20)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')