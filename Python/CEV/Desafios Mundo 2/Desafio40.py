'''Crie um programa que liea duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final, de 
aocrdo com a média atingida
media abaixo de 5.0 = reprovado
meida entre 5.0 e 6.9 = Recuperação
media maior ou igual a 7: Aprovado'''
n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
media = (n1+n2)/2
if media < 5.0:
    print('\033[;31m Reprovado \033[;31m')
elif 5.0 < media < 6.9:
    print('\033[;33m Recuperação \033[;33m')
elif media >= 7:
    print('\033[;32m APROVADO \033[;32m')
