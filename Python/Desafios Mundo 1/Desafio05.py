#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
n=int(input('Digite um número'))
ant = n-1
suc = n+1
print('O número escolhido é {}, seu antecessor é {} e seu sucessor é {}'.format(n, ant, suc))