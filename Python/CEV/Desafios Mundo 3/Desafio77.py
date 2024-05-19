'''Crie um programa que tenha uma tupla com várias palavras
(n usar acentos). Depois disso, você deve mostrar, 
para cada palavra, quais são as suas vogais'''
# Minha Resolução (Não funciona)
'''palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALAHR', 'MERCVADO', 'PROGRAMADOR', 'FUTURO')
contador = 0
c = 0
a=0
e=0
i=0
o=0
u=0
vogaisa = ''
vogaise = ''
vogaisi = ''
vogaiso = ''
vogaisu = ''
while contador < 12:
    l = str(palavras[c])
    if list(palavras[c]) in 'A':
        vogaisa = 'a'
        a +=1
        if a>1:
            vogais = vogais*a
    elif list(palavras[c]) in 'E':
        vogaise = 'e'
        e +=1
        if vogaise > 1:
            vogaise *= e
    elif list(palavras[c]) in 'I':
        vogaisi = 'i'
        i+=1
        if vogaisi > 1:
            vogaisi*=i
    elif list(palavras[c]) in 'O':
        vogaiso = 'o'
        o+=1
        if vogaiso > 1:
            vogaiso *= o
    elif list(palavras[c]) in 'U':
        vogaisu = 'u'
        u+=1
        if vogaisu > 1:
            vogaisu*=u

    print(f'Na palavras {palavras[c]} temos {vogaisa} {
          vogaise} {vogaisi} {vogaiso} {vogaisu}')
    contador += 1
    c += 1      '''
# Resolução Guanabara
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALAHR', 'MERCVADO', 'PROGRAMADOR', 'FUTURO')
for p in palavras:
    print(f'\nNa palavra {p}, temos ', end='')
    # vogais
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
