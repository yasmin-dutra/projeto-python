listSet = {'Gabriel', 'Joao', 'Paulo', 23, 40, 18}
print(f'Lista atual {listSet}')

while True:
    try:
        opcao = str(input('Digite a busca:\n[T] para texto\n[I] para inteiros:\n'))
        opcao = opcao.upper()
        if opcao.isalpha():
            if opcao == 'T':
                escolha = str(input('Qual texto você quer verificar?: '))
                if escolha in listSet:
                    print('Seu texto contém na lista!')
                else:
                    print('Seu texto NÃO contém na lista!')
            elif opcao == 'I':
                escolha = int(input('Qual inteiro você quer verificar?: '))
                if escolha in listSet:
                    print('Seu inteiro contém na lista!')
                else:
                    print('Seu inteiro NÃO contém na lista!')
            else:
                print('Digite uma letra válida')
                continue
        else:
            print('O valor digitado não foi válido!')
    except ValueError as erro:
        print('Digite um valor válido!')
