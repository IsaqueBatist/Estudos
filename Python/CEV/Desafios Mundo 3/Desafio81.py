'''Crie um programa que vai ler vários números e colcar 
em uma lista
Depois mostre
Quantos números foram digitados
A lsita de valores, ordenada de forma decrescente
Se o valor 5 foi digitado e está ou não na lista'''
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opcao = str(input('Quer continuar? [S/N]')).upper()
    while opcao not in 'NS':
        opcao = str(input('Quer continuar? [S/N]')).upper()
    if opcao == 'N':
        break
lista.sort(reverse=True)
print('-='*20)
print(f'No total, foram digitados {len(lista)} Elementos na lista \n A lista de forma decrescente é {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado {lista.count(5)} vezes, nas posiçoes: ', end='')
else:
    print('O valor 5 não foi encontrado dentro da lista')
for a,b in enumerate(lista):
    if b == 5:
        print(a, end=' ')