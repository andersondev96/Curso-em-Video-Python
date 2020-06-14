"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
 e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
"""


def notas(*media, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param media: Uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    informacoes = dict()
    informacoes['maior'] = max(media)
    informacoes['menor'] = min(media)
    informacoes['quantidade'] = len(media)
    informacoes['media'] = sum(media)/len(media)
    if sit:
        if informacoes['media'] >= 7:
            informacoes['situacao'] = 'BOA'
        elif informacoes['media'] >= 5:
            informacoes['situacao'] = 'RAZOÁVEL'
        else:
            informacoes['situacao'] = 'RUIM'

    return informacoes


# Programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
#help(notas)
