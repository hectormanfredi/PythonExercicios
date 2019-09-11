# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

# Para salários superiores a R$1.250,00, calcule um aumento de 10%

#Para os inferiores ou igual, o aumento é de 15%


sal = float(input('Digite o seu salário: R$'))
print('Hoje você ganha R${}'.format(sal))
if sal >= 1251:
    aum = (sal * 10 / 100)
    print('Você ganhou um aumento de 10% no valor de {:.2f}'
          '\n, e a soma do seu aumento com o salário é de {:.2f}'.format(aum, sal + aum))
else:
    aum = (sal * 15 / 100)
    print('Você ganhou um aumento de 15% no valor de {:.2f}'
          '\n, e a soma do seu aumento com o salário é de {:.2f}'.format(aum, sal + aum))
