listSet = set()

for i in range(4):
    num = input('Digite um número: ')
    listSet.add(num)

print(f'Números adicionados pelo usuário: {listSet}')

print(f'Número removido pelo comando pop: {listSet.pop()}')

print(f'Lista atualizada {listSet}')

print('Hora de esvaziar a lista!')

print(f'Lista vazia: {listSet.clear()}')
