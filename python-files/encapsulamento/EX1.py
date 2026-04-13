class Estudante:
    def __init__(self,id,nome):
        self._id = id
        self.nome = nome
        self.__creditos = 1

    @property
    def id(self):
        return self._id
    
    @property
    def creditos(self):
        return self.__creditos
    
    @creditos.setter
    def creditos(self, valor):
        if valor <= 0:
            self.__creditos = 1
        else:
            self.__creditos = valor

    def detalhar(self):
        print(f"ID: {self._id}, NOME: {self.nome}, CREDITOS:{self.__creditos}")

        
e1 = Estudante(1,"mateus")
e1.creditos = 100000
e1.detalhar()

e2 = Estudante(2,"will")
e2.creditos = -1000
e2.detalhar()