'''Desenvolva um porgrama que leia o primeiro termo
e a razão de uma PA. No final, mostre os 1- primeiros
termos da progressão'''
pt = int(input('Primeiro termo:'))
r = int(input('Razão:'))
decimo = pt + (10-1) *r
print('Primeiros dez termos:')
#for c in range(pt, 1 + 10*r, r):
for c in range(pt, decimo + 1, r):
  print(c, end=' -> ')
print('Acabou')
