# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR OU IMPAR

num = int(input('Digite um número: '))
calc = num % 2
if calc == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é ÍMPAR'.format(num))
