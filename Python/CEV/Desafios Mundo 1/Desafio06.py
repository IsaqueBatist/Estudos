# Crie um algoritimo que leia um número e mostre o seu sobro, triplo e raiz quadrada
n = int(input('Digite um número'))
dobro = n*2
triplo = n*3
raiz = n**(1/2)
print('O dobre de {} é {}, seu triplo corresponde à {} e sua raiz é {:.5f}' .format(
    n, dobro, triplo, raiz))
