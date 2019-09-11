# Faça um programa que leia um número qualquer e mostre seu fatorial.

# Ex: 5! = 5x4x3x2x1 = 120
"""
num = int(input('Digite o número para calcular o seu fatorial: '))
c = num - 1
fatorial = num * c
print('{}! = {} x {}'.format(num, num, c), end='')
while not c == 1:
    c = c - 1
    fatorial = fatorial * c
    print(' x {}'.format(c), end='')
print(' = {}'.format(fatorial), end='')
"""

"""
num = int(input('Digite um número para calcular o seu fatorial: '))
c = num - 1
fatorial = num * c
print('{}! = {} x {}'.format(num, num, c), end='')
for r in range(c - 1, 0, -1):
    fatorial = fatorial * r
    print(' x {}'.format(r), end='')
print(' = {}'.format(fatorial))
"""

"""
from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))
"""

num = int(input('Digite um número para calcular o seu fatorial: '))
c = num
fatorial = 1
print('{}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial = fatorial * c
    c = c - 1
print(' = {}'.format(fatorial))
