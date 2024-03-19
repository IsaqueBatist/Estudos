'''Crie uma tupla preenchida com os 20 primeiros colocados
da tabela do Campeonato Brasileiro de Futebol, na ordem 
de colocação. Depois mostre>
Apenas os 5 primeiros colocados
os 4últimos colocados
Uma lista com os times em ordem alfabética
Em que posição na tabela está o time da Chapecoense'''
contador = 1
contadorb = 20
print('=-'*20)
print('{}' .format(' PRIMEIROS COLOOCADOS '))
print('=-'*20)
times = 'Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Brafantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuibá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'Améria-MG'
for c in range(0, 5):
    print(f'{contador}° Colocado - {times[c]}')
    contador += 1
print('=-'*20)
print('{}' .format(' ÚLTIMOS COLOCADOS '))
print('=-'*20)
for b in range(19, 15, -1):
    print(f'{contadorb}° Colocado - {times[b]}')
    contadorb -= 1
print('=-'*20)
print('{}' .format(' ORDEM ALFABÉTICA '))
print('=-'*20)
print(sorted(times))
print('=-'*20)
print(f'O time do VASCO está em {times.index('Vasco')+1}°')
