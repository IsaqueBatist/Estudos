#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
'''from math import sqrt
ca = float(input('Qual o comprimento do cateto adjacente?'))
co = float(input('Qual o comprimento do cateto oposto?'))
h = sqrt(ca**2 + co**2)
print('A hipotenusa do triângulo é {:.2f}' . format(h))'''
ca = float(input('Qual o comprimento do cateto adjacente?'))
co = float(input('Qual o comprimento do cateto oposto?'))
h= (co ** 2 + ca **2 ) ** 2
print('A hipotenusa vai medir {:.2f}' .format(h))