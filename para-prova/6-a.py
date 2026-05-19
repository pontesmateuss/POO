class Clinica:

    def __init__(self):
        # Dicionário de médicos

        # CHAVE = CRM
        # VALOR = objeto médico
        self.lista_medicos = {}

    # Método adicionar médico
    def adicionar_medico(self, medico):

        # Adiciona usando CRM como chave
        self.lista_medicos[medico.crm] = medico

    # Buscar médico pelo CRM
    def buscar_medico_por_crm(self, crm):

        # Verifica se existe
        if crm in self.lista_medicos:
            return self.lista_medicos[crm]
        
        return "Médico não encontrado"
    

# Criando médico
m1 = Medico("Carlos", "1234", "Cardiologista")

# Criando clínica
clinica = Clinica()

# Adicionando médico
clinica.adicionar_medico(m1)

# Buscando médico
print(clinica.buscar_medico_por_crm("1234"))