'''Cir um programa que tenha a função leiaint(), que vai funcionar
de forma semelhando à função input() do Python, só que fazendo
a validação para aceitar apenas um valor numérico'''

# minha resolução

'''def lieaint():
  n = input("Digite um número")
  while True:
   if type(n) == "<class 'int'>":
     break
   elif type(n) == "<class 'str'>":
     print("ERRO! Digite um número inteiro válido")
     n = input("Digite um número")
   elif type(n) == "<class 'float'>":
     print("ERRO! Digite um número inteiro válido")
     n = input("Digite um número")
  print('fim')
lieaint()'''
# Resolução Guanabara


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m Erro! Digite um número inteiro válido. \033[m')
        if ok == True:
            break
        return valor


n = leiaint("Digite um número: ")
