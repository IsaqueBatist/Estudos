# Faça um programa que leia um ângulo qualquer e mostra na tela o valor do seno, cosseno e tangente desse angulo
import math
ang = float(input('Digite um ângulo qualquer'))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O ângulo {} tem o seno de: {:.2f}. \n O cosseno vale: {:.2f} \n E sua tangente vale: {:.2f}' .format(ang,seno, cos, tg))
