from datetime import date


def voto():
    atual = date.today().year
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = atual - nasc
    if idade < 16:
        print('Não apto para votar')
    elif 16 <= idade < 18:
        print('Votação opcional')
    elif 65 <= idade <= 120:
        print('Votação opcional')
    elif 18 <= idade < 65:
        print('Votação obrigatória')
    else:
        print('Idade inválida!')


voto()