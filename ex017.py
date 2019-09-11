# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento
# da hipotenusa.

from math import hypot
catop = float(input('Digite qualquer número para o cateto oposto: '))
catad = float(input('Digite qualquer número para o cateto adjacente: '))
resultado = hypot(catop, catad)
print('O resultado da hipotenusa é: {:.2f}'.format(resultado))

'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''
