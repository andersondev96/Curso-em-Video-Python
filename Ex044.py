"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
"""
print("="*6 ,"LOJAS GUANABARA" ,"="*6)
preco = float(input('Preço das compras: '))
print("FORMAS DE PAGAMENTO")
print("[1] à vista no dinheiro/cheque")
print("[2] à vista no cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")
opcao = int(input('Qual é a opcao? '))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcelas = preco/2
    print('Cada parcela sairá por R${:.2f}'.format(parcelas))
elif opcao == 4:
    parcelas = int(input('Qual é a quantidade de parcelas ? '))
    total = preco + (preco * 20/100)
    valor_parcela = total/parcelas
    print('O valor de cada parcela será R${:.2f}'.format(valor_parcela))
print('O valor a pagar é R${:.2f}'.format(total))
