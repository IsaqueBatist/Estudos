'''Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base da conversão
1 para binário, 2 para octal, 3 para hexadecimal'''
num = int(input('Número inteiro qualquer: '))
print('''Escolha uma das bases para conversão
      [1] Converter para Binário
      [2] Converter para Octal
      [3] Converter apra Hexadecimal''')
esolha = (int(input('Sua opção: ')))
if esolha == 1:
  print('{} convertida para binário é igual a {}' .format(num, bin(num)[2:]))
elif esolha == 2:
  print('{} convertida pra OCTAL é igual a {}' .format(num, oct(num)[2:]))
elif esolha == 3:
  print('{} convertidao para Hexadecimal é igual a {}' .format(num, hex(num)[2:]))
else:
  print('Opção inválida')