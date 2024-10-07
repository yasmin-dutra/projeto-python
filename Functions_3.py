import random


def gerador():
    return random.randint(1, 10)


def principal():
    resposta = gerador()
    #print(resposta)
    print('Palpite Gerado!')
    chute = 0
    while chute != resposta:
        chute = int(input('Digite um número: '))
        if chute > resposta:
            print('Seu palpite foi alto!')
        elif chute < resposta:
            print('Seu palpite foi baixo!')
        else:
            print('Você acertou!')


while True:
    principal()
