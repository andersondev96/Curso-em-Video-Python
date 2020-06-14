"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres
têm menos de 20 anos.
"""
soma = 0
media = 0
velho = 0
menos20 = 0
homem = ''
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma = soma + idade
    if p == 1 and sexo in 'Mm':
        velho = idade
        homem = nome
    if sexo == 'M' and idade > velho:
        velho = idade
        homem = nome
    if sexo == 'F' and idade < 20:
        menos20 += 1
media = soma/4
print('A média de idade do grupo é {:.1f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, homem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(menos20))
