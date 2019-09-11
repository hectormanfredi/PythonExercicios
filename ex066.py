# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o falg).

soma = cont = 0

while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print(f'Você digitou {cont} números e a soma de todos eles é de {soma}')


