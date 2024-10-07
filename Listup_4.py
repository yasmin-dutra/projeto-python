lista = []
while True:
    try:
        for i in range(10):
            num = int(input('Digite um número'))
            lista.append(num)
        lista.sort()
        print(lista)
        lista.sort(reverse=True)
        print(lista)
        break
    except ValueError as erro:
        print('Digite apenas números')
