#O mesmo professor do desafio anterior quer sortar a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteado
'''import random
Aluno1 = 'Gustavo'
Aluno2 = 'Jheniffer'
Aluno3 = 'Higor'
Aluno4 = 'Julia'
o1 = random.randint(1,4)
o2 = random.randint(1,4)
o3 = random.randint(1,4)
o4 = random.randint(1,4)
print('O aluno {} será o {}° \n O aluno {} será o {}° \n o Aluno {} será o {}° \n e o aluno {} será o {}°' .format(Aluno1,o1,Aluno2,o2,Aluno3,o3,Aluno4,o4))'''
from random import shuffle
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno'))
a3 = str(input('Terceiro aluno'))
a4 = str(input('Quarto aluno'))
lista = [a1,a2,a3,a4]
shuffle(lista)
print('A ordem de apresentação será: \n {}' .format(lista))