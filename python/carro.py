class Carro: 
    def __init__(self, marca, modelo, ano):
        self.marca = marca 
        self.modelo = modelo
        self.ano = ano

    def exibir_dados(self):
        print(f"Marca {self.marca}, Modelo {self.modelo}, Ano {self.ano}")

car = Carro("Honda", "Civic", "2026")
car.exibir_dados()

