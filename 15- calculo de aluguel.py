a = float(input('Digite qtos km rodados: '))
d = int(input('Digite a quantidade de dias de aluguel: '))

dia = 60 * d
km_rodado = a * 0.15
total = dia + km_rodado

print ('você alugou o carro por {} dias'.format(d))
print ('você rodou por {}km'.format(a))
print ('Total a pagar é de R$ {}'.format(total))