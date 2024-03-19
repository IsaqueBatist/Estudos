# Listas pt1
'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
num.remove(2) #elemina o 1° elemnto
if 4 in num:
  num.remove(4)
else:
  print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos ')'''
'''valores = []
#ler valores pelo teclado
for cont in range(0,5):
  valores.append(int(input('Digite um valor')))
for v,c in enumerate(valores):
  print(f'Na posição {v} encontrei o valor {c}')
print('Chegeui ao final da lista')'''
a = [2, 3, 4, 7]
# b = a  Ligação de listas
b = a[:] #Cópia da lista A
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
