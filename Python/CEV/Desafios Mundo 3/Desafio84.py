'''Faça um programa que leia o nome e peso de várias pessoas
guardando tudo em uma lista. No final, mostrre:
Quantas pessoas foram cadastradas
Uma listagem com as mais pesadas
Uma listagem com as pessoas mais leves'''
# Minha resolução (PORCA)
'''c = 0
cadastro = []
dados = []
maior = menor = 0
nomemenor = nomemaior = ''
while True:
  cadastro.append(str(input('Nome: ')))
  cadastro.append(int(input('Peso: ')))
  c += 1
  dados.append(cadastro[:])
  opca = str(input('Você quer continuar? [S/N]')).upper()
  while opca not in 'SN':
    opca = str(input('Você quer continuar? [S/N]')).upper()
  if opca == 'N':
    break
for c in dados:
  if c == 0:
    maior = c[1]
    menor = c[1]
    nomemaior = c[0]
    nomemenor = c[0]
  elif c[1] > maior:
    maior = c[1]
    nomemaior = c[0]
  elif c[1] < menor:
    menor = c[1]
    nomemenor = c[0]
print(f'Você cadastrou {c} pessoas \n O maior peso foi de {maior}. Peso de {nomemaior} \n O menor peso foi de {menor}. Peso de {nomemenor}')'''
# Resolução Guanabára
temp = []
principal = []
maio = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        maio = men = temp[1]
    else:
        if temp[1] > maio:
            maio = temp[1]
        elif temp[1] < men:
            men = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Ao todo você cadastou {len(principal)} pessoas.')
print(f'O maior peso foi de {maio}Kg. Peso de ', end='')
for p in principal:
    if p[1] == maio: 
      print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {men}Kg. Peso de ', end='')
for p in principal:
    if p[1] == men:
        print(f'{p[0]}', end= ' ')
