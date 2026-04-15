class Processador:
    def __init__(self, modelo, velocidade):
        self.modelo:str = modelo
        self.velocidade:float = velocidade

class Memoria:
    def __init__(self,capacidade):
        self.capacidade:int = capacidade
        
class Computador:
    def __init__(self, modelo, velocidade, capacidade):
        self.processador = Processador(modelo, velocidade)
        self.memoria = Memoria(capacidade)
    def exibir_configurações(self):
        print(f"Processador: {self.processador.modelo} com {self.processador.velocidade} Ghz e com {self.memoria.capacidade} GB de Memória RAM ")
        
PC = Computador("Intel i9 16900KH", 6.4, 128)
PC.exibir_configurações()