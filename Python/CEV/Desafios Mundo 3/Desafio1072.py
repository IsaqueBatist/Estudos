def aumentar(num, p, form=False):
    f = num*(1+p/100)
    return f if format == False else moeda(f)


def diminuir(num, p, form=False):
    p = num*(1-p/100)
    return p if format == False else moeda(p)


def metade(num, form=False):
    g = num/2
    return g if format == False else moeda(g)


def dobro(num, form=False):
    h = num*2
    return h if format == False else moeda(h)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(m=0, a=10, d=5):
    dp = dobro(m, True)
    mp = metade(m, True)
    ap = aumentar(m, a, True)
    dp = diminuir(m, d, True)
    print('-'*50)
    print(f'{"RESUMO DO VALOR":^50}')
    print('-'*50)
    print(f"Preço analisado \t{moeda(m)}")
    print(f"Dobro do preço \t\t{dp}")
    print(f"Metado do preço \t{mp}")
    print(f"{a}% de aumento \t\t{ap}")
    print(f"{d}% de redução \t\t{dp}")
    print('-'*50)
