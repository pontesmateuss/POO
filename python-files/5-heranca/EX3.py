class Animal:
    def fazer_som(self):
        print("Um Som Desconhecido")

class Cachorro:
    def fazer_som(self):
        print("Latido")

animal_um = Animal()
animal_um.fazer_som()
cachorro_um = Cachorro()
cachorro_um.fazer_som()