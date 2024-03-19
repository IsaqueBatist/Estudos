'''Crie um porgrama que leia vários números inteiros pelo 
telcado, no final da execução mostre a média entre eles
, os valores e qual foi o maior e menos valor. O programa
deve perguntar ao usuário se ele quer o unão continuar a 
digitar valores'''
s = contador = maior = menor = 0
resposta = str('Y')
while not resposta in 'Nn':
    numero = int(input('Digite um número: '))
    s += numero
    contador += 1
    if contador == 1:
         maior = menor = numero
    else:
      if numero > maior:
          maior = numero
      if numero < menor:
          menor = numero
    resposta = str(input('Você deseja continuar? [Y/N]')).strip()
media = s/contador
print('A média final dos {} valores fio de: {:.2f}. Sendo o maior número {} e o menor número {}' .format(contador, media, maior, menor))