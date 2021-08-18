from random import shuffle

a= str(input('Digite o nome do aluno 1: '))
b= str(input('Digite o nome do aluno 2: '))
c= str(input('Digite o nome do aluno 3: '))
d= str(input('Digite o nome do aluno 4: '))

lista = [a,b,c,d]

shuffle(lista)

print('A ordem da apresentação será {}'.format(lista))