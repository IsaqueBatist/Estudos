'''Modifique as funções que foram criadas no desafio107
para que elas ceitem um parâmtro a mais, informando se o 
valor retornado por elas vai ser ou não formatado pela função moeda() 
desenvolvido no desafio 108'''
import Desafio1072
p = float(input('Digite o preço R$'))
print(f'A metade de {Desafio1072.moeda(p)} é {Desafio1072.metade(p,True)}')
print(f'O dobro de {Desafio1072.moeda(p)} é {Desafio1072.dobro(p,True)}')
print(f'Aumentando 10%, temos: {Desafio1072.aumentar(p,10,True)} ')
print(f'Reduzindo 13%, temos: {Desafio1072.diminuir(p,13,True)}')