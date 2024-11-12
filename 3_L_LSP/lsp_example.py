class Animal:
    def comer(self):
        print('O Animal está comendo')

    def andar(self):
        print('O animal está andando na jaula')

class Felino(Animal):
    def lamber(self):
        print('O felino está lambendo seu pelo')

class Leao(Felino):
    def rugir(self):
        print('O leão está rugindo alto!!!')

class Pessoa():
    def observa(self, animal: Animal):
        animal.comer()

pessoa = Pessoa()
animal = Animal()
felino = Felino()
leao = Leao()

animal.comer()
felino.comer()

pessoa.observa(leao)