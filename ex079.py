# Crie um programa onde o usuário possa digitar vários VALORES NUMÉRICOS e cadastre-os em uma LISTA.
# Caso o número já exista lá dentro, ele NÃO SERÁ ADICIONADO.
# No final, serão exibidos todos os VALORES ÚNICOS digitados, em ORDEM CRESCENTE.

valores = list()
copiavalores = list()
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Este valor já existe na lista não ire adicionar')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso')

    opcao = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if opcao == 'N':
        break
print('-=' * 30)
valores.sort()
print(f'Os valores digitados foram: {valores}')


