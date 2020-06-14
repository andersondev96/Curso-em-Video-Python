"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

pessoa = dict()
pessoas = []
soma = 0
media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        opcao = str(input('Quer continuar ? [S/N] ')).upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if opcao in 'Nn':
        break
print('-='*30)

print(f'O grupo tem {len(pessoas)} pessoas cadastradas')
media = soma/ len(pessoas)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista de pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')


