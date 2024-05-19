'''Faça um porgrama que leio o ano de nascimento de um joven
e informe, de acordo com sua idade:
se ele ainda vai se alistar ao serviço militar
se é a hora de se alistar
se já passou do tempo de alistamento'''
from datetime import date
ano = int(input('Em que ano você nasceu?: '))
idade = date.today().year - ano
if idade < 18:
  a = date.today().year - (idade - 18)
  anos = 18 - idade
  print('Você ainda precisa se alistar, e faltam {} anos, em {} ' .format(anos, a))
elif idade == 18:
  print('Você vai se alistar esse ano')
elif idade > 18:
  a = date.today().year - (idade - 18)
  anos = idade - 18
  print('Você já passou do ano de se alistar, já fazem {} anos, em {}' .format(anos, a))