# Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

"""
s = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while s != 'M' and s != 'F':
    if s != 'M' and s != 'F':
        print('Dados inválidos. ', end='')
    s = str(input('Por favor informe o seu sexo [M/F]: ')).upper()
print('Sexo digitado foi {} e ele foi guardado com sucesso.'.format(s))
"""


sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]  # FATIAMENTO, pegando só a primeira letra da string
while sexo not in 'MmFf':
    # [0] FATIAMENTO, pegando só a primeira letra da string
    sexo = str(input('Dados inválidos, por favor informe o seu sexp [M/F]: ')).strip().upper()[0]
print('Sexo informado foi {} e ele foi gravado com sucesso.'.format(sexo))
