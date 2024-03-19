'''Crie um programa onde o usuário possa digitar cinco valores
numéricos e cadastre-os em uma lista, já na posição correta de 
inserção(sem usar sort)
No fianl, mostre a lista ordenada na tela'''
lista = []
for cont in range(0,5):
  a = (int(input('Digite um valor: ')))
  if  cont == 0 or cont > lista[-1]:
    lista.append(a)
    print('Adicionado ao final da lista')
  else:
    pos = 0
    while pos < len(lista):
      if a <= lista[pos]:
        lista.insert(pos, a)
        print(f'Adicionado na posição {pos} da lista')
        break
      pos +=1
print(f'Os valores digitados em ordem foram {lista}')