"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('A média das notas {:.2f} e {:.2f} é igual a {:.2f}'.format(n1, n2, media))
if media >= 7:
    print('Aluno \033[34mAPROVADO')
elif 7 > media >= 5:
    print('Aluno \033[33mEM RECUPERACAO')
else:
    print('Aluno \033[31mREPROVADO')
