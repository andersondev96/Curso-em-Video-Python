"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou
iguais, o aumento é de 15%.
"""
salario = float(input('Digite o salário do funcionario: R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 1 / 10)

print('O novo salário do funcionário que recebia R${:.2f} é R${:.2f}'.format(salario, novo))
