'''Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km\h, mostre uma mensagem dizendo 
que ele foi multado
A multa vai custar R$7 por cada km acima do limite'''
vel = float(input('Qual a velcidade do carro?'))
val = vel - 80
multa = val*7
if vel > 80:
  print('Você está acima da velocidade e foi mutlado em R${:.2f}' .format(multa))
