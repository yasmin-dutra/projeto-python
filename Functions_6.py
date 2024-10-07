import random as r


def geradorInteiros(a, b):
    return r.randint(a, b)


def geradorFloat(x, y):
    return r.uniform(x, y)


def menu():
    while True:
        try:
            opcao = int((input('Digite 1 para inteiro e 2 para reais: ')))
            if opcao == 1:
                x = int(input('Digite o início do intervalo: '))
                y = int(input('Digite o fim do intervalo: '))
                print(geradorInteiros(x, y))
                break
            elif opcao == 2:
                x = float(input('Digite o início do intervalo: '))
                y = float(input('Digite o fim do intervalo: '))
                print(geradorFloat(x, y))
                break
            else:
                print('Opção inválida! Tente novamente.')

        except ValueError as erro:
            print('Entrada inválida, utilize apenas 1 ou 2.')


menu()
