print('Você pode ou não pegar a fila de pririodade?')
condicao = str(input('Qual sua condição?'))

if (condicao == 'idoso') or (condicao == 'cadeirante') or (condicao == 'gestante'):
    print('Pode se dirigir a fila prioritária')
else:
    print('Você não é prioridade!')