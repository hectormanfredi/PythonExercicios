# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa
# vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
# o empréstimo será negado.

cores = {'limpa': '\033[m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m'}
vcasa = float(input('Digite o valor da casa que você quer comprar R$'))
vsal = float(input('Digite o valor do seu salário R$'))
anos = int(input('Em quantos anos você quer pagar? '))
vmensal = vcasa / (12 * anos)
if vmensal <= vsal * 30 / 100:
    print('Parabéns, o seu empréstimo foi {}aprovado!{}'.format(cores['verde'], cores['limpa']))
    print('Valor da parcela R${:.2f}'.format(vmensal))
    print('Quantidade de parcelas: {}'.format(12 * anos))
else:
    print('Infelizmente seu empréstimo {}não foi aprovado{}.'.format(cores['vermelho'], cores['limpa']))


