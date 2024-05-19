'''Crie um programa qeu gerencie o aproveitamento de um jogador
de futebol O progrma vai ler o ome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guaradado
em m dicionário, incluindo o total de de gols feitos durante o campeonato'''
DadosJ = dict()
gols = list()
total = 0
DadosJ['Jogador'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {DadosJ["Jogador"]} Jogou?'))
for c in range(0, partidas):
    gols.append(int(input(f'Quatnos gols na partida {c+1}?')))
    total += gols[c]
    DadosJ['GOLS'] = gols[:]
    DadosJ['Total'] = total
print('-='*30)
print(DadosJ)
print('-='*30)
for e in DadosJ.items():
    print(f'O campo {e[0]} tem o valor {e[1]}')
print('-='*30)
print(f'O jogador {DadosJ["Jogador"]} jogou {partidas} partidas')
for partida in range(0, partidas):
    print(f'=> Na partida {partida+1} fez {DadosJ["GOLS"][partida]} Gols')
print(f'Foi um total de {total} Gols')
print('-='*30)
