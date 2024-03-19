'''Faça um programa que leia o sexo de uma pessoa,
mas só aceite ou valor M ou F; Caso esteja errado, 
peça a digitação novamente até ter um valor correto'''
sexo = str(input('Sexo [M/F]:')).strip()[0]
while not sexo in 'MmFf':
    sexo = str(input('INVÁLIDO, informe o sexo [M/F]: '))
print('Sexo {}, registrado com sucesso' .format(sexo))
