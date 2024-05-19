# Funções
'''def mostralinha():
  print('-='*10)


mostralinha()
mostralinha()
def titulo(txt):
  print('-='*30)
  print(txt)
  print('-='*30)
titulo('oi')'''


def soma(*num):
    s = 0
    for valor in num:
        s += valor
    print(s)
soma(1,2)
soma(3,5,2)
soma(1,3,4,5,6,7,8)

# empacotar parametros
'''def contador (*num):

    for valor in num:
        print(valor, end=' ')
    print()
    print(len(num))
    print(num)
contador(1,2,3,4,5,6,7,8,9,0,)
contador(1,2,3,4,5)
contador(1,2,3,4,12,5,1,2,3,4,76,78,8,45,3,4,5)'''

# função em listas

'''def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos]*=2
        pos+=1 
valores = [5,2,3,4,4]
print(valores)
dobra(valores)
print(valores)'''
