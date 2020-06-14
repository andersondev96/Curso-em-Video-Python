# Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o salário do funcionário? '))
nSalario = salario + (salario * 15/100)
print('O funcionario que recebia R$ {:.2f}, receberá {:.2f} após ter um aumento de 15%. '.format(salario, nSalario))
