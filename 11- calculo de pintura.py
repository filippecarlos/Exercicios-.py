lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = lar * alt
tinta = area / 2

print('A largura da parede é {} e a altura é {} e sua area total é {}'.format(lar, alt, area))
print('A quantidade de titas que será usado será {} litros de tintas' .format(tinta))