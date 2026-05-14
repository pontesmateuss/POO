from abc import ABC, abstractmethod

class Controlavel(ABC):
    @abstractmethod
    def  mover(self):
     pass

class Jogador(Controlavel):
   def mover(self):
      print('jogador se movendo!')

class Volante(Controlavel):
   def mover(self):
      print('girando o volante!')

    
jogador1 = Jogador()
jogador1.mover()

volante1 = Volante()
volante1.mover()
   
