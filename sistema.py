from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'CursoEmVideo.txt'

while True:
    cabecalho('MENU PRINCIPAL')
    resposta = menu(['Criar arquivo', 'Cadastrar pessoa', 'Listar pessoas', 'Sair do sistema'])
    if resposta == 1:
        if not arquivoExiste(arq):
            criarArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = leiaInt('IDADE: ')
        cadastrarPessoa(arq, nome, idade)
    elif resposta == 3:
        lerArquivo(arq)

    elif resposta == 4:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Insira uma opção válida!\033[m')
    sleep(2)
