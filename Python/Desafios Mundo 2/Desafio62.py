'''Melhore o Desafio 61, pergunto para o suário se
ele quer mostrar mais alguns termos. O prgerama 
encerra quando ele disser que quer mostrar 0 termos'''
print('{}' .format('Gerador de PA'))
print('-==-'*5)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
# decimo = pt + (10-1) * r
contador = 1
total = 0
mais = 10
while mais != 0:
  total = total + mais
  while contador <= total:
      print('{}' .format(pt), end=' -> ')
      pt += r
      contador += 1
  print('Pausa')
  mais = int(input('Qantos termos você quer mostrar a mais?'))
print('Progressão finalizada, com {} termos mostrados' .format(total))  
