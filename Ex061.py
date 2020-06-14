"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
print("="*20)
print("10 TERMOS DE UMA PA")
print("="*20)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
n = a1
while c < 10:
    print('{} '.format(n), end='')
    n = n + r
    c += 1

