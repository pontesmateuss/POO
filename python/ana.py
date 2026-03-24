class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

P1 = Pessoa("Ana", "20")

print(f"Nome {P1.nome}, Idade: {P1.idade}")