class Paciente:

    # Método construtor
    def __init__(self, nome, cpf, idade):

        self.nome = nome
        self.cpf = cpf
        self.idade = idade


    # Método para mostrar os dados do paciente
    def exibir_dados(self):

        # Retorna uma string formatada
        return f"Nome: {self.nome} | CPF: {self.cpf} | Idade: {self.idade}"


# Criando objeto
p1 = Paciente("Mateus", "123456", 18)

# Exibindo os dados
print(p1.exibir_dados())