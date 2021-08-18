p = float(input('Digite salario do funcionario: '))
valor_de_acre = 15

res = p + (p * valor_de_acre / 100) # no parentese se calcula a porcentagem e depois tira a diferença
# formula porcentagem ... preço - ( preço * desconto / 100 )

print('O salario dofncionario era R${} com aumento de {} por cento ficará R${} '.format(p,valor_de_acre, res))