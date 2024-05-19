#Faça um programa que leia a largura e a altura de uma parde em metros, calcule a sua área e a quantidade necessária dpara pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
l=float(input('Qual a largura de sua parede?'))
h=float(input('Qual a altura de sua parede?'))
area= l*h
tinta= area//2
resto= area%2
print('Sua parede tem uma área de {}m²,levando em conta que cada litro de tinta cobre uma área de 2m², você precisará de {}L de tinta para pintar a parede toda \n Se o resto: {} for diferente de 0, será necessário mais um litro de tinta' .format(area,tinta, resto))