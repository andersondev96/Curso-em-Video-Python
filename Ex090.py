"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação  em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

notas = dict()

notas['Nome'] = str(input('Nome: '))
notas['Média'] = float(input('Média: '))
if notas['Média'] >= 7.0:
    notas['Situacão'] = 'Aprovado'
elif 5 <= notas["Média"] < 7.0:
    notas['Situacão'] = 'Recuperação'
else:
    notas['Situacão'] = 'Reprovado'
print('-=' *30)
for k, v in notas.items():
    print(f'{k} é igual a {v}')

