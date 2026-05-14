class Animal:
    def emitir_som(self):
        return "Som Desconhecido"
    

class Cachorro(Animal):
    def emitir_som(self):
        return "Auuu AuuuuuU!"
    

class Gato(Animal):
    def emitir_som(self):
        return "MiauuuW!"

animais =[Animal(), Cachorro(), Gato(), Animal(), Cachorro(), Gato()]
print("-" *30)
print("Zoológico Natureza Viva")
print("-" *30)

for animal in animais:
    print(f"{animal.__class__.__name__}: {animal.emitir_som()}")