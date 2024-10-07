def mult(*args):
    total = 1
    for x in args:
        total = total * x
    print(total)


lista = []
num = int(input('Quantas vezes irá repetir?: '))

for i in range(num):
    inteiro = int(input('Digite um número'))
    lista.append(inteiro)

mult(*lista)
