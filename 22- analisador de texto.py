

nome = str(input('Digite seu nome completo: ')).strip() #funçãoque tira os espaços

print('Analisando seu nome ...')

print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem o total de {} letras'.format(len(nome)-nome.count(' '))) # -nome.cont conta os espaços e os elimina do resultado
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))