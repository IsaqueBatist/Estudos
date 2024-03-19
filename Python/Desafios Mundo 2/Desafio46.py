'''Faça um progrma que mostre na tela um contagem refressiva
para os estouros de fogos de artifícios, inde de 10 até 0
com uma pause de 1 segundo entre eles'''
from time import sleep
for c in range(10, 0, -1):
    print('{}!' .format(c))
    sleep(1)
print('\033[;31m BOOOOOOOOOOOOOOMMMMMMMMMMMM \033[;31m')
