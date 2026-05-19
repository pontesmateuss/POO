class Clinica:

    # Método construtor
    def __init__(self, nome):

        # Nome da clínica
        self.nome = nome

        # Lista vazia de pacientes
        self.lista_pacientes = []

        # Lista vazia de médicos
        self.lista_medicos = []


    # Método para adicionar paciente
    def adicionar_paciente(self, paciente):

        # Adiciona o objeto paciente na lista
        self.lista_pacientes.append(paciente)


    # Método para adicionar médico
    def adicionar_medico(self, medico):

        # Adiciona o objeto médico na lista
        self.lista_medicos.append(medico)



class Consulta:

    # Método construtor
    def __init__(self, paciente, medico, data_consulta, horario):

        # Objeto paciente
        self.paciente = paciente

        # Objeto médico
        self.medico = medico

        # Data da consulta
        self.data_consulta = data_consulta

        # Horário da consulta
        self.horario = horario

# Criando paciente
p1 = Paciente("Mateus", "123", 18)

# Criando médico
m1 = Medico("Carlos", "456", "Cardiologista")

# Criando consulta
consulta = Consulta(p1, m1, "10/05", "14:00")


# A Consulta usa objetos Paciente e Medico

# Porém ela NÃO cria esses objetos

# Os objetos continuam existindo
# mesmo sem a consulta

# Isso caracteriza AGREGAÇÃO