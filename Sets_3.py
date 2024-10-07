listSet = {'Joao', 'Paulo', 'Marcus', 'Vinicius'}
print(f'Lista atual: {listSet}')

inc = input('Adicione um nome: ')
listSet.add(inc)
print(f'O nome adicionado foi: {inc}')
print(f'Lista atualizada: {listSet}')

print('-'*30)

rem = input('Remova um nome: ')
listSet.remove(rem)
print(f'O nome removido foi: {rem}')
print(f'Lista atualizada: {listSet}')