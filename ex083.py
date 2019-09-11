# Crie um programa onde o usuário digite uma EXPRESSÃO qualquer que use PARÊNTESES. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e fechados na ORDEM CORRETA.

expr = str(input('Digite a sua expressão: '))
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está INVÁLIDA!')


# TIVE DIFICULDADE DE FAZER ESTE DESAFIO
