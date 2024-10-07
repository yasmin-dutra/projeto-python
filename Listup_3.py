lista = []

while True:
    try:
        for i in range(2):
            num = int(input('Digite um número: '))
            lista.append(num)

        if lista[0] > lista[1]:
            print(f'O maior número é {lista[0]}')
        else:
            print(f'O maior número é {lista[1]}')
        break
    except ValueError as erro:
        print('Apenas números')
