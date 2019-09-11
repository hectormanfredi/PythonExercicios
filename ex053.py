# Crie um programa que leia uma FRASE qualquer e diga se ela é um palíndromo, desconsiderando os espaços
# Ex: APOS A SOPA
#     A SACADA DA CASA
#     A TORRE DA DERROTA
#     O LOBO AMA O BOLO
#     ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: ')).upper().strip().replace(' ', '')
contrario = frase[::-1]
for c in range(0, 1):
    if frase == contrario:
        print('O inverso de {}'.format(frase), end='')
        print(' é {}'.format(contrario))
        print('Esta frase é um palíndromo'.format(frase, contrario))
    else:
        print('O inverso de {}'.format(frase), end='')
        print(' é {}'.format(contrario))
        print('Ou seja, ela NÃO É UM PALÍNDROMO')
