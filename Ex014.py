# Escreva um programa que converta uma temperatura digitada em ºC para ºF

celsius = float(input('Digite uma temperatura em ºC: '))
fareheit = 9 * celsius/5 + 32
print('{}ºC equivale a {:.1f}ºF.' .format(celsius, fareheit))