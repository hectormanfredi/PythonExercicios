# Crie um programa que leia um número Real qualquer pelo teclado e mostre na sua tela a sua porção inteira.

from math import trunc
num = float(input('Digite um número real: '))
print('A parte inteira do número {} é {}'.format(num, trunc(num)))

''' num = float(input('Digite um número real: '))
print('O número digitado foi {} e a sua parte inteira é {}'.format(num, int(num))) '''
