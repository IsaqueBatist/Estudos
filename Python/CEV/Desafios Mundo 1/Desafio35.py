'''Desenvolva um programa que leio o comprimento de 
três retas e diga ao usuário se elas podem ou não formar
um triângulo'''
print('-=' *20)
print('ANALISADOR DE TRIANGULO')
print('-=' *20)
r1 = float(input('Qual o comprimento da primeira reta?'))
r2 = float(input('Qual o comprimento da segunda reta?'))
r3 = float(input('Qual o comprimento da terceira reta?'))
if r1>r2+r3 and r2<r1+r3 and r3<r1+r2:
  print('Os seguimentos acima pode formar um triângulo')
else:
  print('Os seguimentos acima não podem formar um triângulo')