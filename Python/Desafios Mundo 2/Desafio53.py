'''Crie um programa que leia uma frase qualquer e diga
se ela é um palíndromo, desconsiderando os espaços'''
'''frase = str(input('Digite um frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é: {}' .format(frase, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palíndromo')'''
frase = str(input('Digite um frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é: {}' .format(frase, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palíndromo')
