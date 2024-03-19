# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode compar, considere USS1,00 - R$4,27
real=float(input('Quantos reais você têm?'))
dolar = 3.27
valor = real*dolar
print('Se você tem R${}, com o valor do dólar sendo {}, logo, você tem US${:.2f}'.format(real,dolar,valor))
