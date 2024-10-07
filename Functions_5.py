def velocidade_media(dist, tempo):
    return dist / tempo


def menu():
    dist = float(input('Digite a distância percorrida: '))
    tempo = float(input('Digite o tempo: '))
    print(velocidade_media(dist, tempo))


menu()
