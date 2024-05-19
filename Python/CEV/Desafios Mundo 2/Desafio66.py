'''Crie um programa que leia vários números inteiros pelo teclado.
O progrma só vai parar quando o usuário digirtar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles
Desconsiderando o flag'''
s=contador=0
while True:
  numero = int(input('Digite um número [999 para parar]: '))
  if numero == 999:
    break
  s+=numero
  contador +=1
  
print(f'No total, você digitou {contador} números, e sua soma é {s}')