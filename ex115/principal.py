"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome
e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as
pessoas cadastradas.
"""

from ex115.Interface import *
from ex115.Arquivo import *
from time import sleep

arq = 'dados.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar pessoas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt(('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('\033[1;34mSaindo do sitema... Volte sempre!\033[m')

        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)