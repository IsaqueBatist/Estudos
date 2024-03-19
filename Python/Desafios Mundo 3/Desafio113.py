''''Reescreva a função leaint que fizemos no desafio 104, incluinod
agora a possibilidade da digirtação de um número de tipo inválido
Aproveite e cri também a função leafloat() com a mesma funcionaliade
'''


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n

num = leiaInt('Digite um valor inteiro: ')
print(f'O valor digitado foi {num}')
num1 = leiaFloat('Digite um Real ')
print(f'O valor digitado foi {num1}')