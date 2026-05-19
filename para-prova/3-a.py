class Paciente:

    # Método construtor
    def __init__(self, nome, cpf, idade):

        self.nome = nome
        self.cpf = cpf

        # Chamando o setter
        self.idade = idade


    # Getter
    # Método responsável por retornar o valor da idade
    @property
    def idade(self):

        return self.__idade


    # Setter
    # Método responsável por alterar a idade
    @idade.setter
    def idade(self, valor):

        # Verifica se a idade é negativa
        if valor < 11:

            print("cpf inválida!")

        else:

            # Atributo privado
            self.__idade = valor

# O encapsulamento serve para proteger atributos

# O atributo:
self.__idade

# Possui dois underlines (__)

# Isso indica que ele é PRIVADO

# O acesso deve acontecer pelos métodos
# getter e setter



# Criando paciente
p1 = Paciente("Mateus", "123", 18)

# Acessando a idade
print(p1.idade)

# Alterando idade
p1.idade = 20

# Tentando idade negativa
p1.idade = -5

