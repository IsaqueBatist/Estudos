# Cores no terminal
nome = 'isaque'
cores = {'limpa': '\033[m',
         'azul': '\033[34m', }
print('\033[7;30mOlá mundo!\033[m')
print('Olá! Muito prazer em te conhecer, {}{}{}' .format(cores['azul'], nome, cores['limpa']))
'''\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m
\033[m
\033[7;30m'''
