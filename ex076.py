# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Pão', 1, 'Frango', 10.50, 'Chocolate', 5.20, 'Batata', 2)
print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<20}', end='')
    if pos % 2 == 1:
        print(f'R$ {listagem[pos]:>7.2f}')
print('-' * 30)


