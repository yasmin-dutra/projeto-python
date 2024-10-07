nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if nome and idade:
    print(f'Seu nome é: {nome}')
    if ' ' in nome:
        print('Seu nome contém espaços')
        print(f'Seu nome tem {len(nome)} letras')
        print(f'A primeira letra do seu nome é {nome[0]}')
        print(f'A ultima letra do seu nome é {nome[-1]}')
    else:
        print('Seu nome não contém espaços')
        print(f'Seu nome tem {len(nome)} letras')
        print(f'A primeira letra do seu nome é {nome[0]}')
        print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Digite todos os campos')
