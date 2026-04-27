class Veiculo:
     def mover(self): 
        return "Acelerando..."
     

class Moto(Veiculo):
     def mover(self): 
        return "Potência aumentando..."
     

class Carro(Veiculo):
     def mover(self): 
        return "Motor roncando..."
     

class Bicicleta(Veiculo):
     def mover(self): 
        return "Pedalando..."


veiculos = [Veiculo(), Moto(), Carro(), Bicicleta()]
for veiculo in veiculos:
    print(f"{veiculo.__class__.__name__}: {veiculo.mover()}")