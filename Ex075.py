"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
contnove = posicaotres = 0
pares = ()
valor = (int(input('Digite o primeiro valor: ')),
        int(input('Digite o segundo valor: ')),
        int(input('Digite o terceiro valor: ')),
        int(input('Digite o quarto valor: ')))
print(f'Você digitou os valores {valor}')
print(f'O número 9 apareceu {valor.count(9)} vezes')
if 3 in valor:
    print(f'O primeiro número 3 apareceu na {valor.index(3)+1}ª posição')
else:
    print('O número 3 não aparece em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for v in valor:
    if v % 2 == 0:
        print(v, end=' ')
