'''Crie um programa que leia o nome e o preço de vários produtos. O programa 
deverá perguntar se o usuário vai continuar. no final mostre:
Qual é o total gasto
Quantos produtos custam mais de 1000
Qual o nome do produto mais barato'''
total = contador = cont = menor = 0
nomebarato = ''
opcao = ''
while True:
    if opcao == 'N':
        break
    print('-=-'*10)
    nome = str(input('Produto: '))
    preco = float(input('Preço R$'))
    print('-=-'*10)
    cont += 1
    total += preco
    if cont == 1 or preco < menor:
        menor = preco
        nomebarato = nome
    opcao = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while opcao not in 'SNY':
        opcao = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
print('{:-^40}' .format(' FIM DO PROGRAMA '))
print(f'''O total gasto na compra é R${total}
        sendo {contador} produtos custando mais que R$1000 
        Produto mais barato sendo o {nomebarato}, custando R%{menor}''')
