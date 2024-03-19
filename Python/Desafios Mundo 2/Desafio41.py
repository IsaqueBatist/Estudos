'''A confederação Nacio de Natação precisa de um porgrama
que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
ate 9: MIRIM
ate 14: Infantil
ate 19: Junior
ate 20: Senior
maior: master'''
from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
  print('Você é:\033[;36m MIRIM \033[;36m')
elif  9 < idade < 14:
  print('Você é:\033[;36m INFANTIL \033[;36m')
elif 14 < idade < 19:
  print('Você é:\033[;36m Junior \033[;36m')
elif 19 < idade <=25 :
  print('Você é:\033[;36m Sênior \033[;36m')
else:
  print('Você é:\033[;36m Master \033[;36m')