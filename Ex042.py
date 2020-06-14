"""
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""
print('-='*12)
print("ANALISADOR DE TRIÂNGULO")
print('-='*12)
r1 = float(input('Digite o primeiro segmento do triângulo: '))
r2 = float(input('Digite o segundo segmento do triângulo: '))
r3 = float(input('Digite o terceiro segmento do triângulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O segmento pode formar um triângulo')
    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo é ISÓCELES')
    else:
        print('O triângulo é ESCALENO')
else:
    print('Não é possível formar um triângulo')