'''Escreva um programa que pergunte o salário de um 
funcionário e calcule o valor do seu aumento
Para slaários superiores a R$1.250, calcule um aumento de 10%
Para salario infeiores ou iguais, o aumento é de 15%'''
sal = float(input('Qual o seu salário?'))
if sal > 1250:
  aumento = sal + sal*0.01
  print('Seu novo salário com um aumento de 10% é: R${}' .format(aumento))
else:
  aumento = sal + sal*0.15
  print('Seu novo salário com um aumento de 15% é R$:{}' .format(aumento))