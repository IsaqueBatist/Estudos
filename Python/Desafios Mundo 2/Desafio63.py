'''eSCREVA um programa que leia um número n inteiro 
qualquer e mostre na tela os primeiso n elemtnos de uma
fibonacci'''
n = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}' .format(t3), end='')
    t1=t2
    t2=t3
    cont+=1
print(' -> FIM')
