# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(ang))
coseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O angulo de {} tem o seno de {:.2f}'.format(ang, seno))
print('O angulo de {} tem o coseno de {:.2f}'.format(ang, coseno))
print('O angulo de {} tem a tangente de {:.2f}'.format(ang, tangente))

