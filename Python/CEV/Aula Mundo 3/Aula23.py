# Tratamento de erros
try:
    a = int(input("Numerador"))
    b = int(input("Denominador"))
    r = a/b
except (ValueError,TypeError):
    print(f'Tivemos um problema com os tipos de dados')
except ZeroDivisionError:
    print(f'Não é possívelç dividir por 0')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre')
