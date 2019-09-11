# Refaça o DESAFIO 051, lendo o PRIMEIRO TERMO e a RAZÃO de uma PA, mostrando os 10 PRIMEIROS TERMOS da progressão
# usando a estrutura WHILE.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
"""
n = 0
while n != 10:
    n = n + 1
    dez = primeiro + (n - 1) * razao
    print('{} -> '.format(dez), end='')
print('FIM')
"""
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo = termo + razao
    cont = cont + 1
print('FIM')
