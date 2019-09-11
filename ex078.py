# Faça um programa que leia 5 VALORES NÚMERICOS e guarde-os em uma lista.
# No final, mostre qual foi o MAIOR e o MENOR valor digitado e as suas respectivas POSIÇÕES na lista.

valores = list()
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite o valor na posição {c}: ')))
    if c == 0:
        maior = valores[c]
        menor = valores[c]
    elif valores[c] > maior:
        maior = valores[c]
    elif valores[c] < menor:
        menor = valores[c]
print('-=' * 30)
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()







