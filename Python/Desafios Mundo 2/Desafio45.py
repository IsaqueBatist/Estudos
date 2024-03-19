from random import choice
print('\033[33m=-=\033[33m'*10)
print('JOKENPO')
print('\033[33m=-=\033[33m'*10)
jogadas = ['pedra', 'papel', 'tesoura']
jogada1 = str(input('Qual sua jogada?')).lower()
jogada2 = choice(jogadas)
if jogada2 == 'pedra' and jogada1 == 'tesoura':
    print('Eu ganhei!, minha escolha foi {}'.format(jogada2))
elif jogada2 == 'tesoura' and jogada1 == 'pedra':
    print('Você ganhou!, minha escolha foi {}' .format(jogada2))
elif jogada2 == 'papel' and jogada1 == 'pedra':
    print('Ey ganhei!, minha esoclha foi {}' .format(jogada2))
elif jogada2 == 'pedra' and jogada1 == 'papel':
    print('Você ganhou!, minha escolha foi {}'. format(jogada2))
elif jogada2 == 'tesoura' and jogada1 == 'papel':
    print('Eu ganhei!, minha esoclha foi {}' .format(jogada2))
elif jogada2 == 'papel' and jogada1 == 'tesoura':
    print('Você ganhou!, minha esoclha foi {}' .format(jogada2))
elif jogada1 == jogada2:
    print('Empate, eu e você jogamos {}' .format(jogada1))
else:
    print('Opção inválida')
