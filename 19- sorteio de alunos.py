from random import choice

a= str(input('Digite o nome do aluno 1: '))
b= str(input('Digite o nome do aluno 2: '))
c= str(input('Digite o nome do aluno 3: '))
d= str(input('Digite o nome do aluno 4: '))

lista = [a,b,c,d]
escolhido = choice(lista)

print('O aluno escolhido/a foi {}'.format(escolhido))