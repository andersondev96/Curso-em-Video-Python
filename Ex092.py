""""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import date
ano = date.today().year
trabalhador = dict()
trabalhador['Nome'] = str(input('Nome: '))
trabalhador['Idade'] = int(input('Ano de nascimento: '))
trabalhador['Idade'] = ano - trabalhador['Idade']
trabalhador['CTPS'] = int(input('Carteira de trabalho: '))


if trabalhador['CTPS'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentaria'] = trabalhador['Idade'] + ((trabalhador['contratacao'] + 35) - ano)

print('-=' * 30)
for k, v in trabalhador.items():
    print(f'{k} é {v}')


