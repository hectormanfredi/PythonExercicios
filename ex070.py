# Crie um programa que leia o NOME e o PREÇO de vários produtos. O programa deverá perguntar se o USUÁRIO vai continuar.
# No final, mostre:

# A) QUal é o total gasto na compra.
# B) Quantos produtos custam MAIS DE R$ 1000,00
# C) Qual é o nome do produto mais BARATO.
soma = 0
prod1000 = 0
maisbarato = 0
nomeprodmaisbarato = ''
c = 0
print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)
while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto R$:'))
    soma = soma + valor
    if valor > 1000:
        prod1000 = prod1000 + 1
    c = c + 1
    if c == 1:
        maisbarato = valor
        nomeprodmaisbarato = produto
    elif valor < maisbarato:
        maisbarato = valor
        nomeprodmaisbarato = produto
    continuar = str(input('Você deseja continuar [S/N]? ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
    # while True:
    #     if continuar not in 'SN':
    #         continuar = str(input('Você deseja continuar [S/N]? ')).strip().upper()[0]
    #     else:
    #         break
    # if continuar == 'N':
    #     break
print(f'{"FIM":-^40}')
print(f'O valor total da compra é de {soma:.2f}')
print(f'A quantidade de produtos que custam mais de R$1000 são de {prod1000}')
print(f'O nome do produto mais barato foi {nomeprodmaisbarato} que custa R${maisbarato:.2f}')


