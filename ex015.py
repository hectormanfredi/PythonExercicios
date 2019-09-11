# Escreva um programa que pergunte a quantidade de KM percorridos por um carro e a quantidade de dias pelos quais ele
# foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.

qtdkm = float(input('Quantos KM foram rodados? '))
qtddias = int(input('Quantos dias alugados? '))
vfinal = (qtddias * 60) + (qtdkm * 0.15)
print('O total a pagar é de R${:.2f}'.format(vfinal))
