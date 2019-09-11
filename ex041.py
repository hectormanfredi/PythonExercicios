# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# idadeegoria, de acordo com a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

# Style: 0 none / 1 bold / 4 underline / 7 negative
# Text: 30 branco / 31 vermelho / 32 verde / 33 amarelo / 34 azul / 35 magenta / 36 ciano / 37 cinza
# Back: 40 branco / 41 vermelho / 42 verde / 43 amarelo / 44 azul / 45 magenta / 46 ciano / 47 cinza


from datetime import date
cores = {'limpa': '\033[m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'magenta': '\033[1;35m',
         'ciano': '\033[1;36m'}

print('\033[1;34m*-\033[m' * 32)
print('{} Programa de categorização da Confederação Nacional de Natação{}'.format(cores['ciano'], cores['limpa']))
print('\033[1;34m*-\033[m' * 32)

nascimento = int(input('Digite o ano do seu nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento

if idade <= 9:
    print('Você tem {}{}{} anos. Sua categoria é {}MIRIM{}'
          .format(cores['verde'], idade, cores['limpa'], cores['verde'], cores['limpa']))
elif idade <= 14:
    print('Você tem {}{}{} anos. Sua categoria é {}INFANTIL{}'
          .format(cores['amarelo'], idade, cores['limpa'], cores['amarelo'], cores['limpa']))
elif idade <= 19:
    print('Você tem {}{}{} anos. Sua categoria é {}JUNIOR{}'
          .format(cores['azul'], idade, cores['limpa'], cores['azul'], cores['limpa']))
elif idade <= 25:
    print('Você tem {}{}{} anos. Sua categoria é {}SÊNIOR{}'
          .format(cores['ciano'], idade, cores['limpa'], cores['ciano'], cores['limpa']))
else:
    print('Você tem {}{}{} anos. Sua categoria é {}MASTER{}'
          .format(cores['magenta'], idade, cores['limpa'], cores['magenta'], cores['limpa']))
