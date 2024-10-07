nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Qual ingresso você vai escolher? \n 1 - Padrão R$ 20,00 \n 2 - VIP - R$ 50,00 \n')
    escolha = int(input('Digite aqui: '))
    if escolha == 1 or 2:
        print(f'{nome}, ingresso comprado com sucesso!')
    else:
        print('Valor inválido! Tente novamente')
else:
    print(f'{nome}, você não pode participar, é menor de idade!')
