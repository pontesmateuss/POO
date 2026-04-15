class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self,jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        for jogador in self.jogadores:
            print(f"{jogador.nome} - {jogador.posicao}")


jogador_1 = Jogador("Mateus","Armador")
jogador_2 = Jogador("Vitória","Ala")
jogador_3 = Jogador("Will","Pivô")
time_1 = Time("INFO BASQUETE")

time_1.adicionar_jogador(jogador_1)
time_1.adicionar_jogador(jogador_2)
time_1.adicionar_jogador(jogador_3)
time_1.listar_jogadores()