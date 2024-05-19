'''Desenvolva um programa que pergunte a distância de
uma viagem em Km. Calcule o preço da passagem, cobrando
R$0.50 por km para viagem de até 200Km e R$0.45 para 
viagens mais longas'''

km = float(input('Que distância você percorreu em sua viagem?'))
'''if km>=200:
  valor = km/2
  print('O valor cobrado na viagem por {}Km é de R${:.2f}' .format(km, valor))
else:
  valor = km*0.45
  print('O valor cobrado na viagem por {}Km é de R${:.2f}' .format(km, valor))'''
print('Você está preste a começar uma viagem de {}Km' .format(km))
preço = km*0.5 if km <= 200 else km*0.45
print('E o preço da sua passagem será de R${:.2f}' .format(preço))