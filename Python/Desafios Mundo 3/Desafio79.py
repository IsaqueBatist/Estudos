'''Crie um programa onde o usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado
No final, seráo exibidos todos os valores únicos digitados, em ordem crescente'''
# Minha resolução (não funciona)
'''lista= []
while True:
  a = lista.append(int(input('Digite um valor: ')))
  for c, v in enumerate(lista):
    if a == v:
      print('Valor duplicado, não vou registar')
      del(a)
    else:
     print('Valor cadsatrado corretamente')
    opcao = str(input('Quer continuar? [S/N] ')).upper()
  while opcao not in 'SN':
    opcao = str(input('Quer continuar? [S/N] ')).upper()
  if opcao == 'N':
    break
print('-='*20)
print(f'Você digitou os valores {lista}')'''
# Resolução Guanabara
numeros = list()
while True:
  n = int(input('Digite um valor: '))
  if n not in numeros:
    numeros.append(n)
    print('Valor adicionado com sucesso')
  else:
    print('Valor duplicado, não vou adicionar')
  r = str(input('Quer continuar? [S/N]')).upper()
  while r not in 'SN':
    r = str(input('Quer continuar? [S/N]')).upper()
  if r == 'N':
    break
numeros.sort()
print(f'Você digitou os valores {numeros}')