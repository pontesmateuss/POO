class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    def exibir_alunos(self):
        print(f"Os alunos da turma {self.nome}:")
        for aluno in self.alunos:
            print(aluno.nome)

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.turmas = []
    def adicionar_turma(self, nome):
        turma = Turma(nome)
        self.turmas.append(turma)
    def exibir_turmas(self):
        print(f"As turmas da Escola {self.nome}:")
        for turma in self.turmas:
            print(turma.nome)

aluno_um = Aluno("Pontes")
aluno_dois = Aluno("Vitória")
aluno_tres = Aluno("Willian")
aluno_quatro = Aluno("Leite")
turma_um = Turma("INFO2V")

turma_um.adicionar_aluno(aluno_um)
turma_um.adicionar_aluno(aluno_dois)
turma_um.adicionar_aluno(aluno_tres)
turma_um.adicionar_aluno(aluno_quatro)
turma_um.exibir_alunos()

escola_um = Escola("IFRN")
escola_um.adicionar_turma(turma_um.nome)
escola_um.exibir_turmas()