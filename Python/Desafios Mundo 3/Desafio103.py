'''Faça um programa que tenha um função chamada ficha(),
que receba doi parametros opcionais: o nome, de um jogador
e quantos gols ele marcou
O progrma deverá ser capaz de mostrar a ficha do jogador, mesmo
que lagum dadno não tenha sido informado corretamente'''
def ficha(jog='<desconhecido>',gol=0):
  print(f'O jogador {jog} fez {gol} gol(s) no campeonato')

n = str(input("Nome do jogador: "))
g = str(input("Números de gols "))
if g.isnumeric():
  g = int(g)
else:
  g=0
if n.strip() == '':
  ficha(gol=g)
else:
  ficha(n,g)