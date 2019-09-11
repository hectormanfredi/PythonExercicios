# Crie um programa que leia NOME, SEXO e IDADE de VÁRIAS PESSOAS, guardando os dados em um DICIONÁRIO e todos os
# dicionários em uma LISTA. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A MÉDIA de idade do grupo.
# C) Uma lista com todas as MULHERES.
# D) Uma lista com todas as pessoas com IDADE acima da MÉDIA.

dados = dict()
pessoas = list()
idadetotal = 0
media = 0

while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] '))
        if dados['sexo'] in 'MmFf':
            break
        else:
            print('ERRO! Responda apenas M OU F')
    dados['idade'] = int(input('Idade: '))
    idadetotal = idadetotal + dados['idade']
    pessoas.append(dados.copy())
    while True:
        op = str(input('Quer continuar? [S/N]'))
        if op in 'sSnN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if op in 'nN':
        break

media = (idadetotal / len(pessoas))

print(f' - O grupo tem {len(pessoas)} pessoas.')
print(f' - A média de idade é de {media:.2f}')


print(f' - As mulheres cadastradas foram: ', end='')
for i in pessoas:
    if i["sexo"] in 'fF':
        print(i["nome"], end=' ')

print()
print(' - Lista das pessoas que estão acima da média: ')
print()
for i in pessoas:
    if i["idade"] > media:
        for k, v in i.items():
            print(f'{k} = {v};', end='')
        print()

print('<< ENCERRADO >>')




