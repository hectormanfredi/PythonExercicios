# Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO. No início, pergunte ao usuário qual será o
# VALOR A SER SACADO (número inteiro) e o programa vai informar quantas CÉDULAS de cada valor serão entregues.

# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 E R$1.
print('=' * 20)
print(f'{"BANCO CEV":^20}')
print('=' * 20)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
qtdced = 0
while True:
    if total >= ced:
        total = total - ced
        qtdced = qtdced + 1
    else:
        if qtdced > 0:
            print(f'Total de {qtdced} de cédula de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        qtdced = 0
        if total == 0:
            break
print('VOLTE SEMPRE')



