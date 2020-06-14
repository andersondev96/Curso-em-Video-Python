"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
somaColTres = 0
maiorValor = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))

print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            somaPares = somaPares + matriz[l][c]
        if c == 2:
            somaColTres = somaColTres + matriz[l][c]

        if l == 1:
            maiorValor = matriz[1][c]
            if matriz[l][c] > maiorValor:
                maiorValor = matriz[l][c]


print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaColTres}')
print(f'O maior valor da segunda linha é {maiorValor}')

