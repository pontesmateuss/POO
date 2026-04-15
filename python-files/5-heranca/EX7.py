class Veiculo:
     def acelerar(self): 
          print("Acelerando...")

class Moto(Veiculo):
     def acelerar(self): 
          print("Acelerando a cada segundo!")

class Carro(Veiculo):
     def acelerar(self): 
          print("Vrumm Vrummm!")


veiculo_um = Veiculo()
veiculo_um.acelerar()

moto_um = Moto()
moto_um.acelerar()

carro_um = Carro()
carro_um.acelerar()