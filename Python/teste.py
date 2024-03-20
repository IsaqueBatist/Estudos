from math import sqrt
A = float(10.3)
B = float(203)
C = float(5)
# 0.0 20.0 5.0
# 10.3 203.0 5.0
# 10.0 3.0 5.0
x = B*B - 4*A*C
if 2*A != 0 and x > 0:
    R1 = (-B+sqrt(x))/2*A
    R2 = (-B-sqrt(x))/2*A
    print('R1 = {:.5f}' .format(R1/100))
    print('R2 = {:.5f}' .format(R2/100))
else:
    print('Impossível calcular')
