valor = float(input('Quanto você tem na carteira?: '))


def dobro(valor):
    valor = valor * 2
    print(f'Seu valor foi dobrado! Você tem {valor}')


def metade(valor):
    valor = valor / 2
    print(f'Seu valor foi reduzido pela metade, você tem {valor}')


if valor < 50:
    metade(valor)
else:
    dobro(valor)
