'''Crie um programa que tenha uma tupla totalmente preenchida
coom uma contagem por extenso, do zero até vinte.
Seu programa deverá ler um número teclado e mostrá-lo por extenso'''
contagem = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'

while True:
  num = int(input('Digite um número entre 0 e 20: '))
  while not 0<=num<=20:
    num = int(input('Valor inválido, digite um número entre 0 e 20'))
  numero = contagem[num]
  print(f'Você digitou o número {numero}')
  opcao = str(input('Você deseja continuar? [S/N]:' )).upper()
  while opcao not in 'SN':
    opcao =str(input('Não entendi, Você deseja continuar?[S/N]')).upper()
  if opcao == 'N':
    break
