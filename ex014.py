# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

celsius = float(input('Digite uma temperatura em graus celsius: ºC'))
fahrenheit = (celsius * 9 / 5) + 32
print('A temperatura em {:.1f}ºC equivale {:.1f}ºF'.format(celsius, fahrenheit))
