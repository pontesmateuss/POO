class Animal:
    def __init__(self, grupo):
        self.grupo = grupo


class Cachorro(Animal):
    def __init__(self):
        super().__init__("mamífero")

dog = Cachorro()
print(dog.grupo)