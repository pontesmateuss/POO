class Professor:
    def __init__(self, nome, titulacao):
        self.nome = nome
        self.titulacao = titulacao

class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor =[ professor]

    def exibir_informações(self):
        for disciplina in self.professor:
            print(f"Professor: {disciplina.nome}, Disciplina: {self.nome}")

professor_1 = Professor("Leandro", "Mestre")
diciplina_1 = Disciplina("Programação Orientada a Objetos", professor_1)


diciplina_1.exibir_informações()