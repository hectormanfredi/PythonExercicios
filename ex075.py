# Desenvolva um programa que leia QUATRO VALORES pelo teclado e guarde-os em um TUPLA. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

tupla = (int(input('Digite o primeiro um número: ')),
         int(input('Digite o segundo número: ')),
         int(input('Digite o terceiro número:')),
         int(input('Digite o quarto e último número: ')))
num9 = 0
pos3 = 0
print(f'Você digitou os valores {tupla}')
# print(f'O valor 9 apareceu {tupla.count(9)}')
for nove in tupla:
    if nove == 9:
        num9 = num9 + 1
print(f'O valor 9 apareceu {num9} vezes.')
for tres in tupla:
    if tres == 3:
        pos3 = tupla.index(3) + 1
if pos3 > 0:
    print(f'A posição do três é {pos3}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os números pares foram: ', end='')
for pares in tupla:
    if pares % 2 == 0:
        print(pares, end=' ')





