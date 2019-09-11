# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.

continuar = 'S'
num = 0
total = 0
cont = 0
media = 0
maior = 0
menor = 0
while continuar == 'S':
    num = float(input('Digite um número: '))
    total = total + num
    cont = cont + 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    continuar = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
media = total / cont

print('Foram lidos {} números'.format(cont))
print('A soma de todos eles dá {}'.format(total))
print('A média deles é de {}'.format(media))
print('O MAIOR número digitado foi {}'.format(maior))
print('O MENOR número digitado foi {}'.format(menor))
print('FIM')
