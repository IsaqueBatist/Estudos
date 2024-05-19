'''Crie um programa que lia um número inteiro e mostre
na tela se ele é par ou impar'''
num = int(input('Digite um número inteiro qualquer'))
par = num%2
if par == 0:
  print('O número é par')
else:
  print('O número é ímpar')