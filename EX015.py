"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por
Km rodado.

"""

km = float(input('Quantidade de Km percorridos: '))
dias = int(input('Quantidade de dias que foi alugado: '))
preco = (60 * dias) + (0.15 * km)
print('Foram percorridos {} Km em {} dias, por isso o preço que você deverá pagar será de R${:.2f}.'.format(km, dias, preco))
