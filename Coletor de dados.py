print('-'*78)
print('-'*30, 'Coletor de dados', '-'*30)
print('-'*78)

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
nac = str(input('Qual país você nasceu?: '))
hobby = str(input('Qual o seu hobby?: '))

print('Seu nome é', nome)
print(f'Sua idade é: {idade}')
print('Você é nacional do: {}'.format(nac))
print('Seus dados: \n'+ nome + '\n' + str(idade) + '\n' + nac + '\n' + hobby)
