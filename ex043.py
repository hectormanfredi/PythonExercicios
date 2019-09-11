# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
# a tabela abaixo:

# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura ** 2

if imc < 18.5:
    print('Você está ABAIXO DO PESO, o seu IMC é de: {:.1f}.'.format(imc))
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL, o seu IMC é de: {:.1f}'.format(imc))
elif 25 <= imc < 30:
    print('Você está com SOBREPESO, o seu IMC é de: {:.1f}'.format(imc))
elif 30 <= imc < 40:
    print('Você está OBESO, o seu IMC é de: {:.1f}'.format((imc)))
else:
    print('Você tem OBESIDADE MÓRBIDA, procure um médico urgente! {:.1f}'.format(imc))
