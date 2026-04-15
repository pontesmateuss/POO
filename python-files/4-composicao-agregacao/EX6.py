class Comodo:
    def __init__(self, nome, tamanho):
        self.nome:str = nome
        self.tamanho:int = tamanho

class Casa:
    def __init__(self):
        self.comodos:list = []

    def adicionar_comodo(self, comodo):
        self.comodos.append(comodo)

    def listar_comodos(self):
        for comodo in self.comodos:
            print(f"{comodo.nome} com {comodo.tamanho} M²")

comodo_um = Comodo("Quarto", 8)
casa = Casa()

casa.adicionar_comodo(comodo_um)
casa.listar_comodos()