import math

a = float (input('Digite o valor do angulo: '))

seno = math.sin(math.radians(a))
print('O angulo de {} tem o SENO {:.2f}'.format(a, seno))

cosseno = math.cos(math.radians(a))
print('O angulo de {} tem o COSSENO {:.2f}'.format(a, cosseno))

tangente = math.tan(math.radians(a))
print('O angulo de {} tem o COSSENO {:.2f}'.format(a, tangente))
