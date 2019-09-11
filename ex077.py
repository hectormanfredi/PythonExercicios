# Crie um programa que tenha uma TUPLA com VÁRIAS PALAVRAS (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas VOGAIS.

tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMAR', 'FUTURO')
# Este primeiro for ele imprimi cada ELEMENTO da tupla
for palavra in tupla:
    print(f'\nNa palavra {palavra} temos', end=' ')
    # Neste segundo for ele mostra cada letra de cada palavra e verifica se dentro da palavra existe A E I O U
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
