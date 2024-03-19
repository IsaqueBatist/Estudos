from Lib.Interface import *
from time import sleep
from Lib.Arquivo.Manipulacao import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas',
                    'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
       lerArquivo(arq)
    elif resposta == 2:
       cabeçalho('NOVO CADASTRO')
       nome = str(input('Nome: '))
       idade =  leiaInt('Idade: ')
       cadstrar(arq,nome,idade)
    elif resposta == 3:
        cabeçalho('SAINDO DO SISTEMA')
        break
    else:
        print('Erro! Digite uma opção inválida')
    sleep(2)
