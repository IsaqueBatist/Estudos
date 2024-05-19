'''Crie um progrmaa que tenha uma função chamad voto{} que
vai receber como parametro o ano de nascimento de 
uma pessoa, retornando m valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL ou obrigatório nas eleições
negado: <18
opcional: +65
obrigatorio:>=18 '''
def voto(ano=0):
  from datetime import date
  idade = date.today().year - ano
  if idade < 16:
    v = "Voto Negado"
  elif 17<=idade<65:
    v = 'Voto Obrigatório'
  elif idade>65:
    v = 'Voto Opcional'
  print(f'Com {idade} anos: {v}')
ano = int(input("Em que ano você nasceu?"))
voto(ano)