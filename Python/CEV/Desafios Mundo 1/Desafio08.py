#Escreva um programa que leia um valor em metros e o exiba convertida em centímetros e milímetros
metro = int(input('Quantos metros?'))
cen = metro*100
mili = metro*1000
print('Você tem {} metros, logo {} centímetros e {} milímetros' .format(metro,cen,mili))