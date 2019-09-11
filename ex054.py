# Crie um programa que leia o ANO DE NASCIMENTO DE SETE PESSOAS. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.

from datetime import date

anoatual = date.today().year
menores = 0
maiores = 0
for c in range(1, 7 + 1):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    diferenca = anoatual - ano
    if diferenca < 21:
        menores = menores + 1
    else:
        maiores = maiores + 1
print('Maiores de idade: {}'.format(maiores))
print('Menores de idade: {}'.format(menores))

