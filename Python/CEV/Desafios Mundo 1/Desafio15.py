# Escreva um programa que pergunte a qyabtudade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que oc arro custa R$50 por dia e R$0.15 por Km rodado
km = float(input('Quantos Km você percorreu?'))
dia = int(input('Por quantos dias você alugou o carro?'))
vd = dia*60
vkm = km*0.15
print('Foi cobrado R${} pelos {}km percorridos e R${} pelos {} dias alugados, ou seja ao total, você pagará R${}' .format(vkm, km, vd, dia, vd+vkm ))