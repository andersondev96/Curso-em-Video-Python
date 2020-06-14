"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
nascimento = int(input('Digite o seu ano de nascimento: '))
sexo = str(input('Digite o seu sexo: F para femino e M para masculino '))
if sexo == 'F':
    print('Você não precisa se alistar')
else:
    ano_atual = date.today().year
    idade = ano_atual - nascimento
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento,idade,ano_atual))
    if idade > 18:
        print('Você deveria ter se alistado há {} anos'.format(idade-18))
        print('Seu alistamento foi no ano de {}'.format(ano_atual-(idade-18)))
    elif idade < 18:
        print('Ainda faltam {} anos para o seu alistamento'.format(18-idade))
        print('O seu alistamento será no ano de {}'.format(ano_atual+18-idade))
    else:
        print('Você deverá se alistar esse ano')