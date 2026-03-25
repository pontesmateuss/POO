class Estudante:
    identificador = 1

    def __init__(self, id, nome, creditos):
        self.id = id 
        self.nome = nome
        self.creditos = creditos
        Estudante.identificador += 1

    def id_estudante(self):
        print(f"ID do {Estudante.nome}: {Estudante.id}")

    
    id_estudante()