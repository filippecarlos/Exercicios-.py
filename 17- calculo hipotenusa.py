
from math import hypot
a = float(input('Digite o cateto oposto: '))
b = float(input('Digite o cateto adjacente: '))
h = hypot(a,b)
print('A hipotenusa vai ser {:.2f}'.format(h))




'''
a = float(input('Digite o cateto oposto: '))
b = float(input('Digite o cateto adjacente: '))
h = ((a **2 + b **2) ** (1/2))
print('A hipotenusa vai ser {:.2f}'.format(h))
'''