'''Crie um módulo chamado moeda.py que tennha as funções incorporadas 
aumentar(), diminuir(), dobro() e metade()
Faça também um programaq que importe esse módulo e use algumas dessas funçõe'''
import Desafio1072
p = float(input('Digite o preço: RS'))
print(f'A metade de {p} é {Desafio1072.metade(p)}')
print(f'O dobro de {p} é {Desafio1072.dobro(p)}')
print(f'Aumentando 10%, temos: {Desafio1072.aumentar(p,10)} ')
print(f'Reduzindo 13%, temos: {Desafio1072.diminuir(p,13)}')