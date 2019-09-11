# Faça um programa que leia NOME E MÉDIA de um aluno, guardando também a SITUAÇÃO em um DICIONÁRIO. No final,
# mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input('Média: '))

if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situacao'] = 'Recuperação'
else:
    aluno['Situacao'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  -  {k} é igual a {v}')
