# Escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros

m = float(input('Digite a quantidade de metros: '))
c = m * 100
mm = m * 1000
print('{} metro é igual a {:.0f} centimetros ou igual a {:.0f} milimetros'.format(m, c, mm))

