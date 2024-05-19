'''Faça um programa que leia três números e mostre 
qual é o mairo e qual o menor'''
'''n1 = int(input('Digite o primeiro número'))
n2 = int(input('Digite o segundo número'))
n3 = int(input('Digie o terceiro número'))
if n1>n2>n3:
  print('{} é o maior número e {} é o menor número' .format(n1,n3))
if n1>n3>n2:
  print('{} é o maior número e {} é o menor número' .format(n1, n2))
if n2>n1>n3:
  print('{} é o mairo número e {} é o menor número' .format(n2,n3))
if n2>n3>n1:
  print('{} é o maior número e {} é o menor número' .format(n2, n1))
if n3>n1>n2:
  print('{} é o maior número e {} é o menor número' .format(n3, n2))
if n3>n2>n1:
  print('{} é o maior número e {} é o menor número' .format(n3, n1))'''
a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
menor = a
maior = b
if b < a and b<c:
  menor = b
if c > a and c<b:
  menor = c
if a > b and a>c:
  maior = a
if c > b and c>a:
  maior = c
print('O maior valor é: {} E o menor valor é: {}' .format(maior, menor))