# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dele4s e escrevendo o nome do escolhido
'''import random
Aluno1 = 'Gustavo'
Aluno2 = 'Jheniffer'
Aluno3 = 'Higor'
Aluno4 = 'Julia'
sorteio = random.randint(1, 4)
print('Os alunos 1{}, 2{}. 3{} e 4{}, vão ser sorteados, o resultado é: {}' .format(Aluno1, Aluno2, Aluno3, Aluno4, sorteio))'''
from  random import choice
Aluno1 = str(input('Primeiro Aluno:'))
Aluno2 = str(input('Segundo Aluno:'))
Aluno3 = str(input('Terceiro Aluno:'))
Aluno4 = str(input('Quarto Aluno:'))
lista = [Aluno1, Aluno2, Aluno3, Aluno4]
escolhido = choice(lista)
print('O aluno esccolhido foi: {}' .format(escolhido))