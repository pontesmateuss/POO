class Forma:
    def area(self):
        return 0
    
class Retangulo(Forma):
    def area(self, largura, altura):
        return altura * largura
    
forma_um = Forma()
print(forma_um.area())

retangulo_um = Retangulo()
print(retangulo_um.area(14, 10))