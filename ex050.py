# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem PARES.
# Se o valor digitado for ÍMPAR, desconsidere-o.
soma = 0
numpares = 0
# Neste FOR estou pedindo 6 entradas de valores para o usuário
for c in range(1, 6 + 1):
    num = int(input('Digite o {}º valor: '.format(c)))
    # Se o número digitado pelo usuário for par ele será armazenado na lista e depois será somado
    if num % 2 == 0:
        numpares = numpares + 1
        soma = soma + num
print('Você digitou {} números pares e a soma deles é de {}'.format(numpares, soma))

