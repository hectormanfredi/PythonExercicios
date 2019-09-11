# Faça um programa que ajude um jogador da MEGA SENA a criar PALPITES, O programa vai perguntar QUANTOS JOGOS serão
# gerados e vai sortear 6 NÚMEROS ENTRE 1 E 60 para cada jogo, cadastrando tudo em uma LISTA COMPOSTA.
from random import randint
from time import sleep
print('-' * 30)
print(f'{"JOGOS NA MEGA SENA"}')
print('-' * 30)

jogos = list()
numeros = list()

qtd = int(input('Quantos jogos você quer que eu sorteie? '))
for j in range(1, qtd + 1):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
            cont = cont + 1
        if cont == 6:
            break
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()

print(f'-=-=-= SORTEANDO {qtd} JOGOS -=-=-=')
for i, j in enumerate(jogos):
    print(f'Jogo {i + 1}: {j}')
    sleep(1)
print('-=-=-=-= < BOA SORTE! > -=-=-=-=')
