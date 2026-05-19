class Computador:
    def __init__(self, processador, memoria):
        self.processador = processador
        self.memoria = memoria


class Laptop(Computador):
    def __init__(self, processador, memoria, bateria_watts=0):
        super().__init__(processador, memoria)
        self.bateria_watts = bateria_watts


class Desktop(Computador):
    def __init__(self, processador, memoria, cabinete=""):
        super().__init__(processador, memoria)
        self.cabinete = cabinete


laptop = Laptop("Intel i7", 16, 65)
desktop = Desktop("Ryzen 5", 32, "ATX")

print(laptop.processador, laptop.memoria, laptop.bateria_watts)
print(desktop.processador, desktop.memoria, desktop.cabinete)
