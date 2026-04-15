class Autor:
    def __init__(self,autor):
        self.autor = autor

class Livro:
    def __init__(self,nome,autor):
        self.nome = nome
        self.autor = Autor(autor)

    def mostrar_livro(self):
        print(f"o Livro: {self.nome} da autora {self.autor.autor}")
        
livro_um = Livro("Harry Potter: A Pedra Filosofal", "Joanne Rowling")
livro_um.mostrar_livro()