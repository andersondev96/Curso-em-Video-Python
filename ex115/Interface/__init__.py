def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mUsuário preferiu não digitar este número.')
            return 0
        else:
            return num


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f"\033[1;32m{c}\033[m - \033[1;34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt('\033[1;32mSua opção: \033[m')
    return opc

