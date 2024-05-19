'''Crie um programa que leia o nome completo de uma pesso e mostre:
O nome com todoas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo(sem considerar espaços)
Quatas letras tem o primeiro nome'''
nome= str(input('Qual o sue nome completo?'))
print(nome.upper())
print(nome.lower())
print(len(nome.strip()))
nome2 = nome.split()
print(len(nome2[1]))