class Livro:
    def __init__(self, titulo, autor):
        self.titulo:str = titulo
        self.autor:str = autor


class Biblioteca:
    def __init__(self, nome):
        self.nome:str = nome
        self.livros:list = []

    def addlivro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print(f"Na {self.nome} temos os seguintes livros para empréstimo:")
        for livro in self.livros:
            print(f"{livro.titulo} de {livro.autor}")


livro_um = Livro("Harry Potter", "Joanne Rowling")
livro_dois = Livro("Naruto", "Masashi Kishimoto")
livro_tres = Livro("Dragon Ball Z", "Akira Toriyama")

biblioteca_um = Biblioteca("Biblioteca dos Pertencentes")
biblioteca_um.addlivro(livro_um)
biblioteca_um.addlivro(livro_dois)
biblioteca_um.addlivro(livro_tres)
biblioteca_um.listar_livros()