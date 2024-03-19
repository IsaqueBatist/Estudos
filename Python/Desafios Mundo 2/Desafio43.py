'''Desenvolva um alófiac que leio o peso e a alura
de uma pessoa, calcule seu IMC e mostre seu status de
acordo com a tabela abaixo:
<18.5  = abaixo do peso
entre 18.5 e 25: Peso ideial
25 até 30 Sobrepeso
30 ate 40 Obesidade
acima de 40: Obesidade mórbida'''
peso = float(input('Seu peso:'))
altura = float(input('Sua altura:'))
IMC = peso/altura**2
if IMC < 18.5:
  print('Abaixo do peso')
elif 18.5 < IMC < 25:
  print('Peso ideal')
elif 25 < IMC < 30:
  print('Sobrepeso')
elif 30 < IMC < 40:
  print('Obesidade')
else:
  print('Obesidade mórbida')
print('IMC: {:.2f}' .format(IMC))