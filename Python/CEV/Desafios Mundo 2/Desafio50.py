'''Desenvolva um porgrama que leia seis núumeros 
inteiros e mostre a soma apenas daqueles que forem 
pares. Se o valor digitado fo rímpar, desconsidere-o'''
s = 0
cont = 0
for c in range(1,7):
  num = int(input('Digite um número inteiro qualquer'))
  if num%2 == 0:
    s = s + num
    cont = cont +1
print('O valor da soma de todos os {} valores pares é de: {}' .format(cont, s))