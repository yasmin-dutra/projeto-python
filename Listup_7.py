_ = []
impar = []

for i in range(5):
    valor = int(input('Digite um número'))
    if valor % 2 == 1:
        impar.append(valor)
    else:
        _.append(valor)

print(impar)
