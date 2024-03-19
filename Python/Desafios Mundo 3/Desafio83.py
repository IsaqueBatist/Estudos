'''Crie um programa onde o usuário digite uma expressão qualquer que use
parenteses. Seu aplicativo deverá analiser se a expressão apssada
está como sparenteces apertos e fechados na ordem correta'''
expressão = str(input('Digite a expressão:  '))
pilha = []
for c in expressão:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é valida')
else:
    print('Expressão invalida')
