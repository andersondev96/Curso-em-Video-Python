def metade(preco = 0):
    return preco/2


def dobro(preco = 0):
    return preco * 2


def aumentar(preco = 0, taxa = 0):
    nValor = preco * (taxa/100)
    return preco + nValor


def diminuir(preco = 0, taxa = 0):
    nValor = preco * (taxa/100)
    return preco - nValor


def moeda(preco = 0,moeda='R$'):
    return f'{moeda}{preco:>.2f}' .replace('.', ',')
