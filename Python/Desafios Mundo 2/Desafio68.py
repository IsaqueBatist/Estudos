'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só sera interrompido quando o jogardor Perder, mostrando
o total de vitórias consecutivas que ele registou'''
from random import randint
vitorias = 0
r = ''
print('-=-'*10)
print('PAR OU ÍMPAR')
print('-=-'*10)
vencedor = ''
while True:
    if vencedor == 'computador':
        break
    ej = str(input('Você escolhe par ou impar [P/I] ')).upper()
    while ej not in 'PI':
        ej = str(input('Você escolhe par ou impar [P/I] ')).upper()
    nj = int(input(f'Sua escolha é {ej} \nDigite um número entre 0 e 10: '))
    while not 0<nj<10:
        nj = int(input(f'Sua escolha é {ej} \nDigite um número entre 0 e 10: '))
    '''if ej == 'P':
        ec = 'I'
    elif ej == 'I':
        ec = 'P'
    nc = randint(0, 10)
    print('=-'*10)
    soma = nc + nj
    if soma % 2 == 0:
        r = 'PAR'
    else:
        r = 'ÍMPAR'
    if ec == 'I' and soma % 3 == 0:
        print('Você PERDEU')
        vencedor = 'computador'
    elif ec == 'P' and soma % 2 == 0:
        print('Você PERDEU')
        vencedor = 'computador'
    elif ej == 'I' and soma % 3 == 0:
        print('Você VENCEU')
        vencedor = 'jogador'
        vitorias += 1
    elif ej == 'P' and soma % 2 == 0:
        print('Você VENCEU')
        vencedor = 'jogador'
        vitorias += 1'''
    nc = randint(0, 10)
    soma = nc + nj
    if soma % 2 == 0:
        r = 'PAR'
    else:
        r = 'ÍMPAR'
    if ej == 'P':
        if soma % 2 == 0:
            print('Você venceu')
            vitorias+=1
        else:
            print('Você perdeu')
            print(f'Você jogou {nj} e o computador {nc}. O total de {soma} é {r}')
            break
    elif ej == 'I':
        if soma % 3 == 0:
            print('Você ganhou')
            vitorias += 1
        else:
            print('Você perdeu')
            print(f'Você jogou {nj} e o computador {nc}. O total de {soma} é {r}')
            break
    print(f'Você jogou {nj} e o computador {nc}. O total de {soma} é {r}')
print(f'Fim do jogo, você venceu {vitorias} vezes seguidas, foi uma boa maratona')
