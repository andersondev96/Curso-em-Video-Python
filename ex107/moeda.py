def metade(preco):
    return preco/2


def dobro(preco):
    return preco * 2


def aumentar(preco, taxa):
    nValor = preco * (taxa/100)
    return preco + nValor


def diminuir(preco, taxa):
    nValor = preco * (taxa/100)
    return preco - nValor
