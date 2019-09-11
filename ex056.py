# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho.
# - Quantas mulheres tem menos de 20 anos.
c = 0
media = 0
maisvelho = 0
pos = 0
nomemaisvelho = ''
totalmulher20 = 0

for pessoa in range(1, 5):  # laço pessoa no intervalo(1,5)
    print('---- {}ª PESSOA ----'.format(pessoa))
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    c = c + idade
    media = c / pessoa

    if pessoa == 1 and sexo == 'M':
        # pos = pessoa
        maisvelho = idade
        nomemaisvelho = nome
    else:
        if idade > maisvelho and sexo == 'M':  # and pessoa != pos:
            nomemaisvelho = nome
            maisvelho = idade
            # pos = pessoa

    if pessoa == 1 and sexo == 'F' and idade < 20:
        totalmulher20 = totalmulher20 + 1
    else:
        if sexo == 'F' and idade < 20:
            totalmulher20 = totalmulher20 + 1

print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho é o {} que tem {} anos.'.format(nomemaisvelho, maisvelho))
print('Ao todo são {} MULHERES com menos de 20 anos'.format(totalmulher20))

