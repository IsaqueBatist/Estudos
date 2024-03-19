'''Escreva um programa para aprovar o emprestimo bancario
para a compra de uma casa. O programa vai perguntar o 
valor da casa, o salário do comprador e em quantos anos
ele vai pagar
 Calcule o valor da prestação mensal, sabendo que ela não 
 pode exceder 30% do salario ou então o emprestimo será engado'''
vc = float(input('Valor da casa: '))
sl = float(input('Seu salário: R$'))
anos = int(input('Em quantos anos deseja pagar?'))
vm = (vc/(anos*12))
if vm > sl*0.3:
  print('Emprestimo negado')
elif vm < sl*0.3:
  print('O emprestimo foi aprovado e o valor mensão é de R${:.2f}' .format(vm))
