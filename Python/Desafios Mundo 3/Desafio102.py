'''Crie um progrmaa que tenha uma função fatorial() que recea
dois paâmetros: o primeiro que indique o número a calculo e 
o outro chamado show, que será um valor lógico(opcional), indicnado
se será mostrado ou não na tela o processo de cálculo do fatorial'''
from time import sleep


def fatorial(num, show=False):
    '''
    Fatorial(n, show=False)
    ->Calcula o fatorial de um número
    para n: O número a ser calculado
    para show: (opcional) mostrar ou não a conta
    return: O valor do fatorial de um número n
    
    '''
    f = 1
    for c in range(num, 0, -1):
        f *= c
    print(f)
    print("-="*20)
    if show == True:
      for c in range(num, 0, -1):
        if c == 1:
          print(f'{c} ', end="=")
        else:
          print(f'{c} x', end=" ")
      print(f" {f}")
    return f
fatorial(5)
help(fatorial)