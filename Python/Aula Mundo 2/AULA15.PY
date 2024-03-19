# Interropição de while - Break
'''cont = 1
while True:
  print(cont, end=' -> ')
  cont+= 1
print('Acabou')'''
''''s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
      break
    s += n
print('A soma vale {}' .format(s))'''
# fstrings
'''s=0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
      break
    s += n
#print('A soma vale {}' .format(s))
    print(f'A soma vale {s}')'''
nome = 'José'
idade = 33
salario = 987.3523423523523
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}.')
print('O {} tem {} anos e ganha R$ {:.2f}.' .format(nome, idade, salario))
