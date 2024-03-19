'''Adapte o código do desafio 107, criando uma função adicional chamada moeda()
que consiga mostrar os valores mostrar os valores como um valor
monetário formatado'''
import Desafio1072
p = float(input('Digite o preço R$'))
print(f'A metade de {Desafio1072.moeda(p)} é {Desafio1072.moeda(Desafio1072.metade(p))}')
print(f'O dobro de {Desafio1072.moeda(p)} é {Desafio1072.moeda(Desafio1072.dobro(p))}')
print(f'Aumentando 10%, temos: {Desafio1072.moeda(Desafio1072.aumentar(p,10))} ')
print(f'Reduzindo 13%, temos: {Desafio1072.moeda(Desafio1072.diminuir(p,13))}')