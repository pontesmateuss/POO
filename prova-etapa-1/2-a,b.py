class Medico:
    def __init__(self, nome, crm):
        self.nome = nome
        self.crm = crm

class Paciente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Clinica:
    def __init__(self, nome_unidade):
        self.nome_unidade = nome_unidade
        self.__corpo_clinico = []
        self.__lista_pacientes = []

    def adicionar_medico(self, medico: Medico):
        self.__corpo_clinico.append(medico)

    def adicionar_paciente(self, paciente: Paciente):
        self.__lista_pacientes.append(paciente)


class Agendamento:
    def __init__(self, medico: Medico, paciente: Paciente, data_hora: str):
        self.medico = medico
        self.paciente = paciente
        self.data_hora = data_hora


# A Consulta usa objetos Paciente e Medico
# Porém ela NÃO cria esses objetos
# Os objetos continuam existindo
# mesmo sem a consulta
# Isso caracteriza AGREGAÇÃO