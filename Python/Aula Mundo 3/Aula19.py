# Dicionários
'''pessoa = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoa["nome"]}, tem {pessoa["idade"]} anos')
# del pessoa['sexo']
pessoa['nome'] = 'Leandro'
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
for k, v in pessoa.items():
    print(f'o {k} é {v}')'''
'''brasil = []
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''
estado = dict()
brasil = list()
for c in range(0,3):
  estado['uf'] = str(input('Unidade Federativa: '))
  estado['sigla'] = str(input('Sigla do estado: '))
  brasil.append(estado.copy())
print(brasil)
for e in brasil:
  for k, c in e.items():
    print(f'O campo {k} tem valor {c}')
