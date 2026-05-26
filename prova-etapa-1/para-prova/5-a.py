# Importando recursos para classe abstrata
from abc import ABC, abstractmethod


# Classe abstrata
class PessoaClinica(ABC):


    # Método abstrato
    # Obrigatório nas subclasses
    @abstractmethod
    def get_identificacao(self):
        pass


class Medico(PessoaClinica):

    def __init__(self, nome, crm):

        self.nome = nome
        self.crm = crm

    # Implementando método obrigatório
    def get_identificacao(self):

        return f"CRM: {self.crm}" 
    

# Classes abstratas servem como MODELO

# Elas obrigam subclasses
# a implementarem determinados métodos

# Se Medico não implementar:
get_identificacao()

# O Python gera erro