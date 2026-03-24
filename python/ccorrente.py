class ContaCorrente:
    def __init__(self, nome_correntista, cpf_correntista, saldo):
        self.nome_correntista = nome_correntista
        self.cpf_correntista = cpf_correntista
        self.saldo = saldo

    def ContaCorrente(self):
        print(f"Nome: {self.nome_correntista}, CPF: {self.cpf_correntista}, Saoldo: {self.saldo}")

correntista = ContaCorrente("Raimundo", "111.222.333-44", "1000,00")
correntista.metodo()

