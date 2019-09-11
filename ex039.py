# Faça um programa que leia o ano de um nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
cores = {'limpa': '\033[m',
         'verde': '\033[1;32m',
         'azul': '\033[1;34m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m'}

print('\033[1;34m=-=' * 11)
print('{} PROGRAMA DE ALISTAMENTO MILITAR {}'.format(cores['verde'], cores['limpa']))
print('\033[1;34m=-=\033[m' * 11)
sexo = int(input('Digite 1 para sexo MASCULINO e 2 para FEMININO: '))
if sexo == 1:
    anonascimento = int(input('Digite o ano de nascimento: '))
    anoatual = date.today().year
    idade = anoatual - anonascimento
    if idade < 18:
        print('Você tem {} anos e {}NÃO{} precisa se alistar no serviço militar,'
              ' mas faltam {} anos.'.format(idade, cores['amarelo'], cores['limpa'], 18 - idade))
    elif idade == 18:
        print('{}Você tem {} anos e já está na hora de fazer o alistamento no serviço militar.{}'
              .format(cores['vermelho'], idade, cores['limpa']))
    else:
        print('{}Você tem {} anos e já passou {} anos do tempo do alistamento militar.{}'
              .format(cores['verde'], idade, idade - 18, cores['limpa']))
    print('Você está velho pra caralho!')
elif sexo == 2:
    print('O alistamento não é obrigatório para MULHERES.')
else:
    print('Valor inválido, tente novamente!')


