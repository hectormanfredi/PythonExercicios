# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p = float(input('Qual é o preço do produto? R$'))
novo = p - (p * 5 / 100)
print('Este produto custa R${} mas na liquidação este produto está com 5% de desconto e irá custar R${:.2f}'
      .format(p, novo))

