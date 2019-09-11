# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:

# - À vista DINHEIRO / CHEQUE: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
cores = {'limpa': '\033[m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m'}

print('\033[1;32m=$\033[m' * 20)
print('{:^40}'.format('Programa de cálculo de produto'))
print('\033[1;32m=$\033[m' * 20)

valorproduto = float(input('Digite o valor do produto em R$'))
opcaopagamento = int(input('Possuimos as seguintes opções de pagamento:\n'
                           '--------------------------------------\n'
                           '1 - À vista DINHEIRO/CHQUE\n'
                           '--------------------------------------\n'
                           '2 - À vista CARTÃO\n'
                           '--------------------------------------\n'
                           '3 - Em até 2x no cartão de crédito\n'
                           '--------------------------------------\n'
                           '4 - 3x ou mais no cartão de crédito\n'
                           '--------------------------------------\n'
                           'Digite 1, 2, 3 ou 4: '))
if opcaopagamento == 1:
    valorfinal = valorproduto - (valorproduto * 10 / 100)
    print('Você ganhou {}10% de desconto{}, o valor final do produto é de {}R${:.2f}{}'
          .format(cores['verde'], cores['limpa'], cores['verde'], valorfinal, cores['limpa']))
elif opcaopagamento == 2:
    valorfinal = valorproduto - (valorproduto * 5 / 100)
    print('Você ganhou {}5%{} de desconto, o valor final do produto é de {}R${}{}'
          .format(cores['verde'], cores['limpa'], cores['verde'], valorfinal, cores['limpa']))
elif opcaopagamento == 3:
    valorparcela = valorproduto / 2
    print('Você não teve desconto, o valor do produto é de R${:.2f} e o valor da parcela é de R${}'
          .format(valorproduto, valorparcela))
elif opcaopagamento == 4:
    qtdparcela = int(input('Você quer parcelar em {}3, 4, 5, 6, 7, 8, 9, 10, 11 ou 12 vezes?{}\n'
                           'Digite a quantidade de parcelas: '.format(cores['amarelo'], cores['limpa'])))
    valorfinal = valorproduto + (valorproduto * 20 / 100)
    valorparcela = valorfinal / qtdparcela
    print('Nessas condições você tera {}20% de juros{}, o valor do produto ficará em {}R${:.2f}{},'
          ' e o valor da parcela será de {}R${:.2f}{}'
          .format(cores['vermelho'], cores['limpa'], cores['verde'], valorfinal, cores['limpa'],
                  cores['verde'], valorparcela, cores['limpa']))
else:
    print('Opção inválida, repita novamente o processo')
