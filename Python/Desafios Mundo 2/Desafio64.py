'''Crie um programa que leia vários números inteiros pelo
teclado. O programa só vai para quando o usuário digitar o
valor 999, que é condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles'''
b = s = num = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
  b += 1
  s += num
  num = int(input('Digite um número [999 para parar]: '))
print('No final, você digitou {} números, sendo a somas deles é: {}' .format(b,s))

