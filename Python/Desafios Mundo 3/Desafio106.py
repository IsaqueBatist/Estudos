'''Faça um mini-sistema que utilize o interactive help do python. O usuário vai digitar
o comadno e o manual vai aparecer. Quando o usuário digirar a palavra FIM, o programa se encerra
OBS: Use cores'''
c = ('\033[m',
     '\033[0;30;41m'  # vermelho
     '\033[0;30;44m'  # azul
     );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    help(com)
def titulo(msg, cor=0):
    tam = len(msg)+4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('Sistema de Ajuda Pyhelp', 1)
    comando = str(input('Função ou biblioteca'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo("Até Logo!",1 )
