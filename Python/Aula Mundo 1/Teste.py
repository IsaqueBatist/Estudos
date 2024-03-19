'''a = float('5.0')
b = float('7.1')
MEDIA = (a*3.5 + b*7.5)/11
print('MEDIA {:.5}' .format(MEDIA))'''
a,b,c = input().split() 
d,e,f = input().split()
cod = int(a)
num = int(b)
vuni = float(c) 
cod2 = int(d)
num2 = int(e)
vuni2 = float(f)
valor = (num*vuni + num2*vuni2)
print('VALOR A PAGAR: R$ {:.2f}' .format(valor))
