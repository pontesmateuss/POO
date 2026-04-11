from dataclasses import dataclass

@dataclass(frozen=True)
class Estudante:
    def __init__(self, id, nome, creditos):
        self._id = id 
        self.nome = nome
        self.__creditos = creditos
    
    def detalhar(self):
        print(f"{self._id}, {self.nome}")

    def get_creditos(self):
        return self.__creditos
    
    def set_creditos(self, valor):
        if valor <= 0:
            self.__creditos = 1
        else: 
            self.__creditos = valor

    def detalhar(self):
        print(f"nome: {self.nome}")
        print(f"id: {self._id}")
        print(f"créditos: {self.__creditos}")

#atributos
estudante1 = Estudante(1, "Kobe")
estudante2 = Estudante(2, "LeBron")
#metodo
estudante1.get_creditos(200)
estudante2.set_creditos(100)

estudante1.get_creditos(100)
estudante2.set_creditos(50)
#detalhamento
estudante1.detalhar()
estudante2.detalhar()