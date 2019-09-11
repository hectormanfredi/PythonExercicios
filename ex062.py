# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. o Programa encerra quando
# ele disser que quer mostrar 0 TERMOS.

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '. format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos mais você quer? '))
print('Progressão finalizada, foram mostrados {} termos.'.format(total))




