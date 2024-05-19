'''Faça um programa que tenha uma função chamada átea(), que
receba as dimens~es de um terreno retangular e 
mostre a area do terreno'''


def area(a, n):
    s = a * n
    print(f"A area de um terreno{a}x{n} é de {s:.2f}m² ")


largura = float(input("Largura(M)"))
comprimento = float(input("Comprimento(m)"))
area(largura, comprimento)
