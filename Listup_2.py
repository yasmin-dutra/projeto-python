lista = []
for i in range(3):
    compras = input('Digite sua fruta! ')
    lista.append(compras)

if 'banana' in lista:
    print('Temos essa fruta!')
else:
    print('Fruta indisponível')
