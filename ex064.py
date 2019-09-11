# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# desconsiderando o flag.

n = 0
soma = 0
total = 0
c = 0
n = int(input('Digite um número: '))
while n != 999:
        soma = n
        total = (total + soma)
        c = c + 1
        n = int(input('Digite um número: '))
print('Foram digitados {} números e a soma deles é de {}'.format(c, total))

