class Consulta:
    def __init__(self, paciente, medico):
        self.paciente = paciente
        self.medico = medico

    # Método da classe mãe
    def exibir_dados(self):
        return f"Consulta presencial com {self.medico.nome}"
    
#

# Classe filha
class ConsultaOnline(Consulta):
    # Sobrescrevendo método
    def exibir_dados(self):

        return f"Consulta ONLINE com {self.medico.nome}"
    
#

# Criando objetos
consulta1 = Consulta(p1, m1)

consulta2 = ConsultaOnline(p1, m1)

# Chamando métodos
print(consulta1.exibir_dados())

print(consulta2.exibir_dados())

#

# Polimorfismo significa:
# mesmo método -> comportamentos diferentes

# O método:
exibir_dados()

# Existe nas duas classes

# Porém cada classe executa de forma diferente