'''Faça um programa que leia um número qualquer e
mostre seu fatorial'''
# from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
# f = factorial(num)
c = num
f = 1
print('Calculadno {}! ' .format(num), )
while c > 0:
    print('{}' .format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}' .format(f))
    
