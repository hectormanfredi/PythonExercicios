# Faça um programa que leia NOME E PESO de VÁRIAS PESSOAS, guardando tudo em uma LISTA. No final, mostre:
# A) QUANTAS pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais PESADAS.
# C) Uma listagem com as pessoas mais LEVES.

dado = list()
pessoas = list()
maior = 0
menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = dado[1]
        menor = dado[1]
    elif dado[1] > maior:
        maior = dado[1]
    elif dado[1] < menor:
        menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    opcao = str(input('Quer continuar: [S/N]'))
    if opcao in 'Nn':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas no total.')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()






