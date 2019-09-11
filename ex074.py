# Crie um programa que vai gerar CINCO NÚMEROS ALEATÓRIOS e colocar em uma TUPLA.
# Depois disso, mostre a LISTAGEM DE NÚMEROS gerados e também indique o MENOR e o MAIOR valor que estão na tupla.

from random import sample
num = sample(range(1, 10), 5)
print(f'Os números sorteados foram {num}')
print(f'O maior valor foi {max(num)}')
print(f'O menor valor foi {min(num)}')




