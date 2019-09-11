# Aprimore o DESAFIO ANTERIOR, mostrando no final:
# A) A SOMA de todos os VALORES PARES digitados.
# B) A SOMA dos valores da TERCEIRA COLUNA.
# C) O MAIOR valor da SEGUNDA LINHA.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = 0
somatercol = 0
maiorlinha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar = spar + matriz[l][c]
    print()
print('-' * 30)
print(f'A soma dos valores pares é de {spar}')
for l in range(0, 3):
    somatercol = somatercol + matriz[l][2]
print(f'A soma dos valores da terceira coluna é de {somatercol}')
for c in range(0, 3):
    if c == 0:
        maiorlinha = matriz[1][c]
    elif matriz[1][c] > maiorlinha:
        maiorlinha = matriz[1][c]
print(f'O maior valor da segunda linha é {maiorlinha}')
