# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas letras minusculas
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome: ')).strip()
print('Nome digitado {}, e ele com todas as letras maiusculas: {}'.format(nome, nome.upper()))
print('Nome digitado {}, e ele com todas as letras minusculas: {}'.format(nome, nome.lower()))
print('Quantidade de letras que possui o nome sem espaços {}'.format(len(nome) - nome.count(' ')))
# print('O primeiro nome tem {} letras'.format(nome.find(' ')))
separador = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separador[0], len(separador[0])))
