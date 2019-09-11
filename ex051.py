# Desenvolva um programa que leia o PRIMEIRO TERMO(elemento) e a RAZÃO(constante) de uma PA (Progressão Aritmética).
# No final, mostre os 10 primeiros termos dessa progressão.
# formula: an = a1 + (n - 1) * r onde an é o número do termo e n é a quantidade de termos que queremos

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
dez = primeiro + (10 - 1) * razao  # formula
for c in range(primeiro, dez + razao, razao):
    print('{} '.format(c), end='-> ')
print('FIM')

"""
a1 = 5
a2 = 5 + 2 = 7 
a3 = 7 + 2 = 9 
a4 = 9 + 2 = 11 
a5 = 11 + 2 = 13 
a6 = 13 + 2 = 15 
a7 = 15 + 2 = 17 
"""

# tive um pouco de dificuldade neste exercicio
