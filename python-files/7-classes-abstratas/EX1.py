import tkinter as tk, abstractmethod

Controlavel = tk.Tk()
Controlavel.title("Minha Interface")
# Texto na tela (Label)
mover = tk.Label(Controlavel, text="Jogador se movendo...")
mover.pack(padx=200, pady=200)
# Botão
mover_2 = tk.Button(Controlavel, text="Mover", command=lambda: print("Volante girando"))
mover_2.pack()

class Jogador(Controlavel):
    def __init__(self):
        










Controlavel.mainloop()
