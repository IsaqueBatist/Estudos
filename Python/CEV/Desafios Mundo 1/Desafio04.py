#Faça um programa que leia algo pelo teclado e mostre na telas eu tipo primitivo e todas as informações possíveis sobre ele
texto = input('Digite algo')
print( type(texto))
print(texto.isalpha())
print(texto.isnumeric())
print(texto.isalnum())