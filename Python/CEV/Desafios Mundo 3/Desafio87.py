'''Aprimore o desafio anterior, mostrando no final:
a soma de todos os valores pares digitados
a soma dos valores da terceira coluna
o maior valor da segunda linha'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = mai = somac = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
    print()
print('-='*20)
print(f'A soma dos valores pares é: {somap}')
for l in range(0, 3):
    somac += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {somac}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        maior = matriz[1][c]
print(f'O maior número da segunda linha é {maior}')