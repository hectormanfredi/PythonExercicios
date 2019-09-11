# Crie um programa que leia NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os (com IDADE) em um DICIONÁRIO
# se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ANO DE CONTRATAÇÃO e o SALÁRIO. Calcule
# e acrescente, além da IDADE, com quantos anos a pessoa vai se APOSENTAR.

from datetime import date

trabalhador = dict()

trabalhador['nome'] = str(input('Nome: '))
trabalhador['idade'] = int(input('Ano de Nascimento: '))
trabalhador['idade'] = (date.today().year - trabalhador['idade'])
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contracao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$ '))
    trabalhador['aposentadoria'] = (trabalhador['contracao'] + 35) - (date.today().year - trabalhador['idade'])

print('-=' * 30)
# print(trabalhador)

for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')

