# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Digite o salário do funcionário: R$'))
aum = (sal * 15 / 100)
print('O funcionário recebeu um aumento de 15% equivalente a R${:.2f} e agora passa a receber R${:.2f}.'
      .format(aum, sal+aum))
