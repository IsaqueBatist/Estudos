'''Faça um programa que tenha uma função chamada contador()
que receba tres parametros, inicio, fim e passo,
e realize a contagem
Seu progrmaa tem que realizar tres contagens atraves da função criada
de 1 ate 10 de 1 em 1
de 10 ate 0 de 2 em 2 
uma contagem personalizada'''

# minha resolução
'''def contagem(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if passo < 0:
        passo *= -1
    if passo == 0:
      passo = 1
    if inicio > fim:
        valor = inicio
        print(valor, end=" ")
        while valor > fim:
            valor -= passo
            print(valor, end=" ")
    else:
        valor = inicio
        print(valor, end=" ")
        while valor < fim:
            valor += passo
            print(valor, end=" ")


contagem(1, 10, 1)
print()
print("-"*20)
contagem(10, 0, 2)
print()
print("-"*20)
a = int(input("Digite o inicio da contagem: "))
b = int(input("Digite o fim da contagem: "))
c = int(input("Digite o passo da contagem: "))
print("-"*20)
contagem(a, b, c)'''
# resilução guanabara




from time import sleep
def contador(i, f, p):
    print("-="*20)
    print(f"Contagem de {i} até {f} de {p} em {p}")
    if p < 0:
        p*= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end="", flush=True)
            sleep(0.5)
            cont += p
        print("FIM")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont -= p

contador(1, 10, 1)
contador(10, 0, 2)
print()
print("-="*20)
print("\nAgora é sua vez de personalixaar a contagem")
ini = int(input("Inicio: "))
fim = int(input("Fim: "))
pas = int(input("Passo:"))
contador(ini,fim,pas)