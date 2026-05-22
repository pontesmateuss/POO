class Medico:

    def __init__(self, nome, crm, especialidade):

        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade


    # Método especial __str__
    # Define como o objeto será exibido
    def __str__(self):

        return f"Médico: {self.nome} | CRM: {self.crm} | Especialidade: {self.especialidade}"


# Criando objeto
m1 = Medico("Carlos", "1234", "Pediatra")

# Exibindo objeto
print(m1)