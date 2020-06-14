"""
Crie um programa que tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um valor
literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
OBRIGATÓRIO nas eleições.
"""

from datetime import date


def voto(ano_nasc):
    idade = date.today().year - ano_nasc

    if 18 <= idade < 65:
        return f'Com {idade} anos. VOTO OBRIGATÓRIO!'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos. VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos. NÃO VOTA!'


# Programa principal
print('-'*30)
ano_nasc = int(input('Em que ano você nasceu? '))
result = voto(ano_nasc)
print(result)
