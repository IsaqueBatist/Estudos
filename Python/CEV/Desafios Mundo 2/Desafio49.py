'''Refaça o Desafio 9 mostrando a tabuada de um número 
que o usuário escolher, só que agora utilizando um laço for'''
n = int(input('Que tabuada deseja consultar?: '))
for c in range(1,n+1):
  r= n*c
  print('{} x {} = {}' .format(n,c,r))