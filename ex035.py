# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triângulo.

rt1 = float(input('Digite o valor da primeira reta: '))
rt2 = float(input('Digite o valor da segunda reta: '))
rt3 = float(input('Digite o valor da terceira reta: '))

if (rt2 - rt3) < rt1 < rt2 + rt3 and (rt1 - rt3) < rt2 < rt1 + rt3 and (rt1 - rt2) < rt3 < rt1 + rt2:
    print('É possível formar um tringulo')
else:
    print('This is impussibru!')

