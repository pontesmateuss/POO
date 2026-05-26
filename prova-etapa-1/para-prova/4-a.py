# Classe base
class Pessoa:

    # Método construtor
    def __init__(self, nome, telefone):

        self.nome = nome
        self.telefone = telefone

# Paciente herda Pessoa
class Paciente(Pessoa):

    # Método construtor
    def __init__(self, nome, telefone, cpf, idade):

        # Chama o construtor da classe pai
        super().__init__(nome, telefone)

        # Atributos próprios da classe Paciente
        self.cpf = cpf
        self.idade = idade



# O super() chama métodos da classe pai

# Nesse caso:
super().__init__(nome, telefone)

# Está chamando o construtor da classe Pessoa

# Evita repetição de código