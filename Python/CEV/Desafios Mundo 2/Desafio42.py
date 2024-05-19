''''Refaça o desfio35 do striângulos, acrescentando 
o recurso de mostrar qu etipo de tri^nagulop será formado
Equilatero: todos iguais
Isóceles: dois lados iguais
Escaleno: todos os lados diferentes'''
l1 = float(input('Comprimento do primeiro lado: '))
l2 = float(input('Comprimento do segundo lado: '))
l3 = float(input('Comprimento do terceiro lado: '))
tipo = 'Equilatero'
if l1 == l2 != l3 or l2 == l3 != l1 or l1 ==l3!=l2:
  tipo = 'Isóceles'
elif l1 != l2 != l3:
  tipo = 'Escaleno'
if l1 < l2+l3 and l2 <l1+l3 and l3<l1+l2:
  print('O triangulo EXISTE e seu tipo é: {}' .format(tipo))
else:
  print('Esse triângulo não EXISTE')