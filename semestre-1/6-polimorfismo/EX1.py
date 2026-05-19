class Animal:
    def emitir_som(self):
        return "Som Desconhecido"
    

class Cachorro(Animal):
    def emitir_som(self):
        return "Auu AuuuuuU!"
    

class Gato(Animal):
    def emitir_som(self):
        return "Miauw"
    

animais =[Animal(), Cachorro(), Gato()]
for animal in animais:
    print(f"{animal.__class__.__name__}: {animal.emitir_som()}")