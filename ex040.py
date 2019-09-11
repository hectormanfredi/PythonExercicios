# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:

# - Média abaixo de 5.0:
# REPROVADO

# - Média entre 5.0 e 6.9:
# RECUPERAÇÃO

# Média 7.0 ou superior:
# APROVADO
cores = {'limpa': '\033[m',
         'amarelo': '\033[1;33m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('Você está {}REPROVADO!{} Sua média foi de: {}{:.1f}{}'
          .format(cores['vermelho'], cores['limpa'], cores['vermelho'], media, cores['limpa']))
elif media >= 5 and media < 7:
    print('Você está de {}RECUPERAÇÃO!{} Sua média foi de {}{:.1f}{}'
          .format(cores['amarelo'], cores['limpa'], cores['amarelo'], media, cores['limpa']))
else:
    print('Você foi {}APROVADO!{} Sua média foi de: {}{:.1f}{}'
          .format(cores['verde'], cores['limpa'], cores['verde'], media, cores['limpa']))
