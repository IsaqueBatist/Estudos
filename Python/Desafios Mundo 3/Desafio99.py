''''Faça um progrmaa que tenha uma função  chamada maior(), que
receba vários parâmetros com valores itneiros
seu programa tem que analisar todos os valores e dizer qual deles é o maior'''


def maior(*num):

    maior = menor = 0
    for p, v in enumerate(num):
        if p == 0:
            maior = v
        if v > maior:
            maior = v

    print("-="*20)
    print(f"Analisando so valores passados...")
    print(f"{num} foram informados {len(num)} valores ao todo")
    print(f"O maior valor inforamdo foi {maior}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
