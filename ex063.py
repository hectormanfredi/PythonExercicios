# Escreva um programa que leia um NÚMERO N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# SÊQUENCIA DE FIBONACCI.
# Ex: 0 -> 1 -> 1 -> -> 2 -> 3 -> 5 -> 8
#    t1   t2   t3
n = int(input('Digite a quantidade de termos que você quer mostrar: '))
t1 = 0
t2 = 1
t3 = t1 + t2
c = 3
print('{} - {}'.format(t1, t2), end='')
while c <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c = c + 1
print(' -> FIM')
