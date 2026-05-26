# Classe Paciente
class Paciente:

    # Método construtor
    # Executado automaticamente quando o objeto é criado
    def __init__(self, nome, cpf, idade):

        # self representa o próprio objeto

        # Atributo nome
        self.nome = nome

        # Atributo cpf
        self.cpf = cpf

        # Atributo idade
        self.idade = idade


# Classe Medico
class Medico:

    # Método construtor
    def __init__(self, nome, crm, especialidade):

        # Nome do médico
        self.nome = nome

        # CRM do médico
        self.crm = crm

        # Especialidade do médico
        self.especialidade = especialidade