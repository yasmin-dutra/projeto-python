print('-'*38)
print('Calculadora de IMC'.center(35))
print('-'*38)

peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)

if imc >= 40:
    print('Obesidade mórbida')
elif (imc < 40) and (imc >= 30):
    print('Obesidade')
elif (imc < 30) and (imc >= 25):
    print('Sobre peso')
elif (imc < 25) and (imc >= 20):
    print('Peso normal')
elif (imc < 20) and (imc >= 25):
    print('Peso normal')
