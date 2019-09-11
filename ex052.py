# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# números primos são números naturais que tem apenas dois divisores diferentes, o 1 e ele mesmo.
cores = {'limpa': '\033[m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'azul': '\033[1;34m'}
num = int(input('Digite um número: '))
primo = 0

# O for faz a contagem de divisoes, iniciando em 1 até o valor digitado pelo usuário
for divisor in range(1, num + 1):
    # O if verifica se o resto da divisão do número é igual a 0
    # , e ai adiciona um valor a variavel primo que é um contador
    if num % divisor == 0:
        primo = primo + 1
        print('{}{} {}'.format(cores['verde'], divisor, cores['limpa']), end='')
    # Aqui se a condição acima for falsa não será adicionado valor algum na variavel primo
    else:
        print('{}{} {}'.format(cores['vermelho'], divisor, cores['limpa']), end='')
print('\n{}TOTAL {} vezes {}'.format(cores['azul'], primo, cores['limpa']))
# Aqui faço a verificação final, onde se a variavel primo for maior que dois então ele não é um número PRIMO senão
# o número digitado é um número primo
if primo == 2:
    print('O número {} foi divisivel apenas {} vezes, portanto {}ELE É PRIMO{}'
          .format(num, primo, cores['verde'], cores['limpa']))
else:
    print('O número {} foi divisivel {} vezes, portando ele {}NÃO É PRIMO{}'
          .format(num, primo, cores['vermelho'], cores['limpa']))


