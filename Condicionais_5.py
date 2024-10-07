print('-' * 25 + 'Cardápio' + '-' * 25)

dog = 'Cachorro quente'
burguer = 'Hambúrguer'
coxa = 'Coxinha'

print('Código', 'Especificação', 'Valores', sep='\t\t\t\t')
print('100', '|', dog, '|', 'R$ 5,00', sep='\t\t')
print('101', '|', burguer.center(18), '|', 'R$ 10,00', sep='\t\t')
print('102', '|', coxa.center(18), '|', 'R$ 4,00', sep='\t\t')
print('-' * 58)

cod = int(input('Informe o código do pedido:'))
qtd = int(input('Informe a quantidade'))


if cod == 100:
    print(f'Pedido: {dog} \nQuantidade: {qtd} \nValor total: R$:{qtd * 5} ')
elif cod == 101:
    print(f'Pedido: {burguer} \nQuantidade: {qtd} \nValor total: R$:{qtd * 10} ')
elif cod == 102:
    print(f'Pedido: {dog} \nQuantidade: {qtd} \nValor total: R$:{qtd * 4} ')
else:
    print('Informe um código válido')
