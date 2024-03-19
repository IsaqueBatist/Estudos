# TEORICA
'''
def contador(i, f, p):
    """Faz uma contagem
    I: Iniico
    F: final
    p: passo
    """
    c = i
    while c <= f:
        print(c, end="")
        c += p
# Variavel opcional


def somar(a, b, c=0):
    s = a + b + c
    print(s)
# escolpo de variavel

    def teste():
        x = 8  # escopo loca, funciona so na função
        print(f"Na função teste, n vale {n}")
        print(f"Na função teste, x vale {x}")


n = 2  # escopo global
print(f"No programa principal, n vale {n}")
#print(f'no programa principal, x vale {x}')
# retorno de valores
def somar (a=0,b=0,c=0): 
	s = a+b+c
	return s
resultado1 = somar(3,2,5)
resultado2 = somar(1,7)
resultado3 = somar(4)
print(f'Os resultados foram {resultado1} {resultado2} {resultado3}.')
'''
# PRATICA
def fatorial(num=1):
  f = 1
  for c in range(num, 0, -1):
  	  f *= c
       return f 


n= int(input('DiGITE UM NÚMERO'))
print(f"O fatorial de {n} é igual a {fatorial(n)}")

def parouimpar(n=0):
     if n%2==0:
      return True
     else:
      return False
     