'''Crie um programa que lia nome, ano de nasciment e carteira de trabalho e ca
dastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zaro,
o dicionário receberá também o ano de contratação e o salario. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar'''
from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['ano de nascimento'] = int(input('Ano de Nascimento: '))
idade = datetime.today().year - cadastro['ano de nascimento']
cadastro['Idade'] = int(idade)
a = int(input('Carteira de trabalho: (0 não tem): '))
if a != 0:
    cadastro['ano de contratação'] = int(input('Ano de contratação'))
    cadastro['salario'] = float(input('Salário R$ '))
    cadastro['aposentadoria'] = cadastro['Idade'] + ((cadastro['ano de contratação']+35) - datetime.today().year)
print('-='*20)
for e in cadastro.items():
    print(f'{e[0]} tem o valor de {e[1]}')
