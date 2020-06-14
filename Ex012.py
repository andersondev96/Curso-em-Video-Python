# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Preço do produto: R$ '))
desconto = preco - (preco*0.05)
print('O novo preço do produto que custava R${:.2f} com 5% de desconto e R$ {:.2f} '.format(preco, desconto))