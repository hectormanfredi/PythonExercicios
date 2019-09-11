# Faça um programa que leia o peso de CINCO PESSOAS. No final, mostre qual foi o MAIOR e o MENOR peso lidos.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa KG:'.format(p)))
    # O primeiro valor sempre será o maior e o menor, já que ainda não existem outros valores
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é de Kg{}'.format(maior))
print('O menor peso é de Kg{}'.format(menor))

