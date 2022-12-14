def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mTivemos um erro com os tipos de dados que você inseriu!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário decidiu não informar os dados!\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    c = 1 
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(linha())
    resp = leiaInt('\033[35mSua opção:\033[m ')
    return resp
