'''Faça um programa que tenha uma função chamada escreva()
que recena um texto qualquer como parametro e mostre
uma menssagem com tamanho adaptavel'''
def escreva(txt):
  tam = len(txt)+4
  print(f"{'~'*tam}")
  print(f"  {txt}")
  print(f"{'~'*tam}")
escreva("oi")
escreva("Gustavo Guanabra")
escreva("Curso de pyhtoin no Youtube")
