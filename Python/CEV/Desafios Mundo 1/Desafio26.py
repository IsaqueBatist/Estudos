'''Faça um programa que leia uma frase pelo teclado e
mostre
quantas vezes aparece a letra A
em que posição el aaparece a primeira vez
em que posição ela aparece a últma vez'''
frase=str(input('Digite uma frase qualquer')).upper().strip()
print('Quantas vezes aparece a letra "A"?: {} vezes' .format(frase.count('A')))
print('Em que posição ela aparece pela primeira vez? : {}' .format(frase.find('A')+1))
print('Em que posição ela aparece pela última vez? : {}' .format(frase.rfind('A')+1))