'''Crie um programa qonde o usuário possa digitar sete 
valores numéricos e castre-os em uma listá única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares
e impares em ordem crescente'''
num = [[], []]
valores = []
for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*20)
num[0].sort()
num[1].sort()
print(f'Todos os valores: {num} \nValores pares {
      num[0]} \nValores ímpares {num[1]}')
