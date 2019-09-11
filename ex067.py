# Faça um programa que mostre a tabuada de vários números, um de cada vez, para da valor digitado pelo usuário.
# O programa será INTERROMPIDO quando o número solicitado for negativo.

while True:
    print('-' * 35)
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    multiplicador = 0
    res = 0
    if tabuada < 0:
        break
    while multiplicador < 10:
        multiplicador = multiplicador + 1
        res = tabuada * multiplicador
        print(f'{tabuada} x {multiplicador} = {res}')
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')



"""
while True:
    print('-' * 30)
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if tabuada < 0:
        break
    for c in range(1, 11):
        res = tabuada * c
        print(f'{tabuada} x {c} = {res}')
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
"""








