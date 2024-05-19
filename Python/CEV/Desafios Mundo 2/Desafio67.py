'''Faça um programa que mostre a tabuada de vários números
, um de cada vez, para cada valor digitado pelo usuário. O 
programa deverá ser interrompido quando o número solicitado
for negativo'''
a = 1
num = 1
num = int(input('Quer ver a tabuada de qual valor?'))
while True:
  if num < 0:
      print('Parando programa...')
      break
  print('-'*10)
  '''while a <= 10:
    resultado = num * a
    print(f'{num} x {a} = {resultado}')
    a+=1
  a = 1'''
  for c in range(1,11):
     print(f'{num} X {c} = {num*c}')
  print('-'*10)
  num = int(input('Quer ver a tabuada de qual valor?'))

    