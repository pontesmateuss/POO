# Criando exceção personalizada
class PacienteNaoEncontradoError(Exception):
    pass


class Clinica:
    def __init__(self):

        # Lista de pacientes
        self.lista_pacientes = []

    # Método para buscar paciente
    def buscar_paciente_por_cpf(self, cpf):

        # Percorre a lista
        for paciente in self.lista_pacientes:

            # Verifica CPF
            if paciente.cpf == cpf:
                return paciente

        # Caso não encontre
        raise PacienteNaoEncontradoError("Paciente não encontrado!")
    

try:
    # Tentando buscar paciente
    clinica.buscar_paciente_por_cpf("123")

# Captura o erro
except PacienteNaoEncontradoError as erro:
    print(erro)


# raise
# Serve para lançar exceções

# try
# Tenta executar o código

# except
# Captura erros caso aconteçam