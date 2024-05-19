'''Aprimore o desafio 93 para que ele funcione com vários jogadores
incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador'''
# minha resolução (PERDIDA)
'''Dados = {}
gols = []
jogadores = []
while True:
    total = 0
    Dados['Nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {Dados['Nome']} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols n partida {c+1}? ')))
        total += gols[c]
    Dados['GOLS'] = gols[:]
    Dados['TOTAL'] = total
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    jogadores.append(Dados.copy())
    Dados.clear()
    gols.clear()
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper()
    if opcao == 'N':
        break
print('=-'*20)
print('{:<10}{:<15}{:^15}{:>15}' .format('N°', 'Nome', 'GOLS', 'TOTAL'))
for c in range(0, len(jogadores)):
    print(f'{c:<10}{jogadores[c]["Nome"]:<15}{jogadores[c]["GOLS"]:^20}{jogadores[c]["TOTAL"]:>15}')
while True:
    escolha = int(input('Mostrar dados de qual jogador? [999 para parar]'))
    if escolha == 999:
        break
    for c in range(o,len(jogadores[escolha]["GOLS"])):
        print(f'LEVAMTAMENTO DO JOGADOR {jogadores[escolha]}:')
        print(f'No jogo {} fez {} gols')'''
'''Crie um programa qeu gerencie o aproveitamento de um jogador
de futebol O progrma vai ler o ome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guaradado
em m dicionário, incluindo o total de de gols feitos durante o campeonato'''
time = list()
DadosJ = dict()
gols = list()
total = 0
while True:
    DadosJ.clear()
    gols.clear()
    DadosJ['Jogador'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {DadosJ["Jogador"]} Jogou?'))
    for c in range(0, partidas):
        gols.append(int(input(f'Quatnos gols na partida {c+1}?')))
        total += gols[c]
        DadosJ['GOLS'] = gols[:]
        DadosJ['Total'] = total
        time.append(DadosJ.copy())
    resp = str(input('Quer continuar? [S/N]')).upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
    if resp == 'N':
        break
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
