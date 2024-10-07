nome = input('Digite seu nome')
sexo = input('Digite seu sexo [M] ou [F]')
sexo = sexo.upper()
ec = input('Digite seu estado civil')

print(f'Nome: {nome}')

if sexo == 'M':
    print('Sexo: Masculino')
    print(f'Estado civil: {ec}')
elif sexo == 'F':
    print('Sexo: Feminino')
    print(f'Estado civil: {ec}')
else:
    print('Digite um valor válido para o sexo!')



