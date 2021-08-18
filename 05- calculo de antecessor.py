# Faça um programa que leia seunumero int e mostre na tela seu antecessor e sucessor

#Versão1
n = int(input('digite um número: '))
antecessor = n-1
sucessor = n+1

print('Analisamos o valor {}, e verificamos que o seu antecessor é {}, e seu sucessor é {}'.format(n,antecessor, sucessor))


#Versão2
n = int(input('digite um número: '))

print('Analisamos o valor {}, e verificamos que o seu antecessor é {}, e seu sucessor é {}'.format(n,n-1, n+1))

