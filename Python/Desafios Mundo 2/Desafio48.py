'''Faça um programa qu ecalcule a soma entre todos os 
números ímpares que são múltiplos de três e que se 
encontrem no intervalo de 1 até 500'''
s = 0
cont = 0
for c in range(1,501, 2):
  if c%3 == 0:
    s = c + s
    cont= cont +1
print('A soma de todos os {} números ímpares e divisível por 3 entre 1 e 500 é: {}' .format(cont,s))