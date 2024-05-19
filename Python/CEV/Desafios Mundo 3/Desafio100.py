'''Faça um progrma que tenha uma lista chamada numeros 
e fuas funç~eos chamadas sorteia() e somaPar(). A primeira
função vai sortear 5 números e vai colocá-los dentro da lista
e a sunda função vai mostrar a soma entre todos os valores pares sorteados
pela função anteior'''
from random import randint
numeros = []
def sorteia():
  for c in range (0,5):
    numeros.append(randint(0,10))
  print(f"Sorteando 5 valores da lista: {numeros}")
def somaPar():
  s = 0
  for p,v in enumerate(numeros):
    if v % 2 == 0:
      s+= v
  print(f"Somando so valores pares de {numeros}, temos {s}")
sorteia()
somaPar()
