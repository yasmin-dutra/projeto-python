print('Você é obrigado a votar?')
nome = str(input('Qual seu nome? \n'))
idade = int(input('Qual a idade? \n'))

if (idade >= 18) and (idade <=65):
    print('Você precisa votar!, vá apertar 13')
else:
    print('Você ainda não tem idade suficiente!')
