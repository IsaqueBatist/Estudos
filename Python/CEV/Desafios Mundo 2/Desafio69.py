'''Crie um programa que leia a idade de e o sexo de várias pessoas
A cada pessoa cadastrada, o prigrama deverá perguntar se ao usuário
quer ou não continuar. NO final, mostre
Quantas pessoas tem mai de 18 anos
Quantos homens foram cadastrados
Quantas mulheres tem menos de 20 anos'''
maior = homenscadastrados = mulheresnovas = 0
escolha = ''
print('-=-'*10)
print('{:-^20}' .format('CADESTRE UMA PESSOA'))
print('-=-'*10)
while True:
    print('='*5)
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input('[M/F]: ')).upper().strip()
    print('='*5)
    escolha = str(input('Você deseja continuar [Y/N]?')).upper().strip()
    while escolha not in 'YNS':
        escolha = str(input('Você deseja continuar [Y/N]?')).upper().strip()
    if escolha == 'N':
        break
    if idade >= 18:
        maior += 1
    if sexo == 'F' and idade < 20:
        mulheresnovas += 1
    if sexo == 'M':
        homenscadastrados += 1
print(f'No total {maior} pessoas tem mais de 18 anos, {
      homenscadastrados} homens foram cadastrados e {mulheresnovas} mulheres tem menos de 20 anos')
