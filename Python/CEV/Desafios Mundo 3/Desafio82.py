'''Crie um prgrama que vai ler vários números e colocar em uma lista
Depois disso, cri duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente
Ao final, mostre o conteúdo das três listas geradas'''
l1 = []
l2 = []
l3 = []
while True:
  a = (int(input('Digite um valor:')))
  l1.append(a)
  if a % 2 == 0:
     l2.append(a)
  else:
     l3.append(a)
  opcao = str(input('Quer continuar [S/N]? ')).upper()
  while opcao not in 'SN':
      opcao = str(input('Quer continuar [S/N]? ')).upper()
  if opcao =='N':
    break
print(f'A lista com todos os números é: {l1} \nA lista com todos os números pares é {l2} \nE a lista com todos os números ímpares é: {l3}')