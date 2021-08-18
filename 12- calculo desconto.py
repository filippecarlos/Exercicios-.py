p = float(input('Digite o preço do produto: '))
valor_desconto = 5

res = p - (p * valor_desconto / 100) # no parentese se calcula a porcentagem e depois tira a diferença
# formula porcentagem ... preço - ( preço * desconto / 100 )

print('O produto que custava R${} com desconto de {} por cento ficará R${} '.format(p,valor_desconto, res))