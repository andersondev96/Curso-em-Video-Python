""""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente.
"""
listanum =  list()
opcao = ' '

while True:
    n = int(input('Digite um valor: '))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opcao = str(input('Quer continuar ? [S/N] '))
    if opcao in 'Nn':
        break
print('-='*30)
listanum.sort()
print(f'Você digitou os valores {listanum}')


