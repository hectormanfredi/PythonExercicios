# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o seu nome: ')).strip()
print('O nome digitado foi: {}, e tem SILVA nele?| {} | FALSE para Não e TRUE para Sim'.format(nome, 'SILVA' in nome.upper()))