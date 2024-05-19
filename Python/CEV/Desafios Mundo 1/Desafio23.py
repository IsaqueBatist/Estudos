'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados 
Ex: digite um número: 1834
Unidade:4
dezena:3
centena8
milhar:1'''
num = str(input('Digite um número inteiro'))
print('Unidade : {}' .format(num[3]))
print('Dezena : {}' .format(num[2]))
print('Centena : {}' .format(num[1]))
print('Milhar : {}' .format(num[0]))




