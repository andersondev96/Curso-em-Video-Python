def metade(preco = 0, formato=False):
    res = preco/2
    return res if not formato else moeda(res)


def dobro(preco = 0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def aumentar(preco = 0, taxa = 0, formato=False):
    nValor = preco * (taxa/100)
    res = preco + nValor
    return res if formato is False else moeda(res)


def diminuir(preco = 0, taxa = 0, formato=False):
    nValor = preco * (taxa/100)
    res = preco - nValor
    return res if formato is False else moeda(res)


def moeda(preco = 0,moeda='R$'):
    return f'{moeda}{preco:>.2f}' .replace('.', ',')
