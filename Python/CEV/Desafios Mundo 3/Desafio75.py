'''Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final mostre:
Quantas vezes apareceu o valor 9
Em que posição foi digitado o primeiro valor 3
Quais foram os números pares'''
# minha resolução (PODRE)
'''from random import randint
contador = 0
numeros = ''
pares = ''
while contador <4:
  num = str(randint(0,10))
  numeros += num + ' '
  contador += 1
  a = int(num)
  if a % 2 == 0:
    pares = str(a) + ' '
print(pares)
print(f'Na sequência de números: {numeros}, o valor 9 aparceu {numeros.count('9')} vezes, O valor 3 apareceu na posição {numeros.index('3')}. Os números pares são: {pares}')'''
# Resolução Guanabara
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
  print(f'O valor 3 apareceu na posição {num.index(3)+1}')
else:
   print('O valor 3 não foi digitado')
print(f'Os valores digitados foram: ', end='')
for n in num:
    if n != 0:
      if n % 2 == 0:
          print(n, end=' ')
