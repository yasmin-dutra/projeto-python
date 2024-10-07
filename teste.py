"""class Bola:
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca
        print('Valores Iniciais: ', self.cor, self.marca)

    def mudarCor(self):
        self.cor_bola = input('Informe uma nova cor: ')
        print(f'A cor anterior é: {self.cor}')
        print(f'A nova cor é: {self.cor_bola}')

cor = input('Digite uma cor: ')
marca = input('Digite uma marca: ')
objeto = Bola(cor, marca)
objeto.mudarCor()"""


"""class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        print(self.nome, self.idade, self.altura, self.peso)
"""


class Animal:
    def __init__(self, nome_animal, idade_animal):
        self.nome = nome_animal
        self.idade = idade_animal

    def __info(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade} ano(s)')

    def dormir(self):
        print('Animal que gosta muito de dormir')


class teste_super(Animal):
    def __init__(self, nome_animal, idade_animal, name):
        super().__init__(nome_animal, idade_animal)
        self.name = name

    def __info(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade} ano(s) {self.name}')

    def mostrar(self):
        self.__info()


objeto = teste_super('animal 1', 2, 'Gatinho')
objeto.mostrar()
