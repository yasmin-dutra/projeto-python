def somarNumeros(n1, n2, n3):
    return n1 + n2 + n3


def calculaMedia(soma):
    return soma/3


def menu():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    print('Soma:', somarNumeros(n1, n2, n3))
    print('Média:', calculaMedia(somarNumeros(n1, n2, n3)))

menu()

