tupla = (5, 'b', True)

lista = list(tupla)

lista.append('string')

tupla = tuple(lista)

print(tupla)
print(type(tupla))
