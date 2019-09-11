# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

real = float(input('Quantos reais você tem na sua carteira? R$'))
dolar = real / 3.85
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
