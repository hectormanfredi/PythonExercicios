# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio de 10 ATÉ 0,
# com uma pausa de 1 segundo entre eles.

from time import sleep
from emoji import emojize

print('CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFICIO')
for c in range(10, 0 - 1, -1):  # (inicio, fim, iteração)
    print(c)
    sleep(1)
print(emojize(':fireworks:' * 10))
