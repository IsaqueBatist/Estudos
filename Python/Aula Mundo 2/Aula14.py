# Estrutura de repetição WHILE
'''for c in range(1,11):
  print(c)
print('FIM')
d=1
while d < 10:
 print(d)
 d += 1
print('FIM')'''
n=1
cp = 0
ci = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
      if n%2 == 0:
        cp+=1
      else:
        ci+=1
print('O número todal de pares foi de: {} números pares e o de ímpares foi de {} números' .format(cp,ci))