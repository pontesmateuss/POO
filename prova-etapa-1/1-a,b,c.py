class Medico:
    def __init__(self, nome1, especialidade1, crm1):
        self.nome1 = nome1
        self.especialidade1 = especialidade1
        self.crm1 = crm1

    def apresentar_medico(self):
        print(f"NOME: {self.nome1}, ESPECIALIDADE: {self.especialidade1}, CRM: {self.crm1}")

class Paciente:
    def __init__(self, nome, cpf, contato):
        self.nome = nome
        self.cpf = cpf
        self.contato = contato
    
    def exibir_informacoes(self):
        print(f"NOME: {self.nome}, CPF: {self.cpf}, CONTATO: {self.contato}")


dadosM = Medico("Mateus", "Cirurgião", "000101")
dadosM.apresentar_medico()

dadosP = Paciente("Pontes", "111.222.333-44", "8499212121")
dadosP.exibir_informacoes()
