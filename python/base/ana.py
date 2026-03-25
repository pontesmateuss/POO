class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Ana", "20")

print(f"Nome: {p1.nome}; Idade: {p1.idade}")