# Crie um programa que leia a IDADE e o SEXO de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o USUÁRIO quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos HOMENS foram cadastrados.
# C) quantas MULHERES tem menos de 20 anos.

maior18 = 0
homens = 0
mulhermenor20 = 0
while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
    while True:
        if sexo not in 'MF':
            sexo = str(input('Valor inválido. Digite o seu sexo [M/F]: ')).strip().upper()[0]
        else:
            break
    if idade > 18:
        maior18 = maior18 + 1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        mulhermenor20 = mulhermenor20 + 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total de pessoas com mais de 18 anos é de {maior18}')
print(f'O total de homens cadastrados é de {homens}.')
print(f'O total de mulheres menores de 20 anos é de {mulhermenor20}')
print('Programa finalizado')

