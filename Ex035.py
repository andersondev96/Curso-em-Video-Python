"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
 se elas podem ou não formar um triângulo.
"""
print('-='*12)
print("ANALISADOR DE TRIÂNGULO")
print('-='*12)
r1 = float(input('Digite o primeiro segmento do triângulo: '))
r2 = float(input('Digite o segundo segmento do triângulo: '))
r3 = float(input('Digite o terceiro segmento do triângulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O segmento pode formar um triângulo')
else:
    print('Não é possível formar um triângulo')