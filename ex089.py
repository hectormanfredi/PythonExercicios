# Crie um programa que leia NOME e DUAS NOTAS de vários alunos e guarde tudo em uma LISTA COMPOSTA.
# No final, mostre um BOLETIM contendo a MÉDIA de cada um e permita que o usuário possa mostrar as NOTAS de cada
# aluno individualmente.
"""
from time import sleep

classe = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    classe.append(dados[:])
    dados.clear()
    opcao = str(input('Quer continuar? [S/N] '))
    if opcao in 'Nn':
        break

media = list()
for p in classe:
    dados.append(p[0])
    dados.append((p[1] + p[2]) / 2)
    media.append(dados[:])
    dados.clear()

print('-=' * 30)
print('No.     Nome             Média')
print('------------------------------')

for i, p in enumerate(media):
    print(f'{i:<1} {p[0]:>12} {p[1]:>13}')

while True:
    print('-' * 26)
    opcao2 = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao2 == 999:
        print('FINALIZANDO...')
        sleep(1)
        print('<<< VOLTE SEMPRE >>>')
        break
    elif opcao2 > len(classe) - 1:
        print('Aluno inexistente')
    elif opcao2 <= len(classe) - 1:
        print(f'Notas de {classe[opcao2][0]} são [{classe[opcao2][1]}] [{classe[opcao2][2]}]')
"""
# Solução Professor

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    opcao = str(input('Quer continuar? [S/N] '))
    if opcao in 'Nn':
        break

print('-=' * 30)
print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>10}')
for i, p in enumerate(ficha):
    print(f'{i:<4} {p[0]:<10} {p[2]:>10.1f}')

while True:
    print('-' * 30)
    opcao2 = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao2 == 999:
        print('FINALIZANDO...')
        break
    elif opcao2 > len(ficha) - 1:
        print('Aluno não existe, tente novamente!')
    elif opcao2 <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao2][0]} são {ficha[opcao2][1]}')
print('<<< VOLTE SEMPRE >>>')

