# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

# A multa vai custar R$ 7,00 por cada Km acima do limite.

v = float(input('Digite a sua velocidade: '))
if v > 80:
    print('Você foi multado! Você excedeu o limite permitido de 80km/h')
    m = (v - 80) * 7
    print('O valor da multa foi de R${}'.format(m))
print('Tenha um bom dia! Dirija com segurança.'.format(v))
