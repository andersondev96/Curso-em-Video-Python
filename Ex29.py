"""
29.	Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 Km/h,
 mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 para cada Km acima do limite.

"""

velocidade = float(input('Digite a velocidade do carro em Km/h: '))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print('Você foi multado! Estava andando {:.0f} Km acima do limite permitido e sua multa  é de R$ {:.2f}' .format(velocidade-80, multa))
