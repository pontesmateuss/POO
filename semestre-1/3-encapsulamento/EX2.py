class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0

  
    def depositar(self, valor):
        if valor <= 0:
            print("Valor de um depósito Inválido")
        else:
            self.__saldo += valor
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo Inválido ou insuficiente")

    def consultar_saldo(self):
        return self.__saldo
    
    def detalhar(self):
        print(f"TITULAR: {self.titular} SALDO: {conta_um.consultar_saldo()}")
    

conta_um = ContaBancaria("Mateus Pontes", )
conta_um.depositar(1000)
conta_um.sacar(67)

conta_um.detalhar()
conta_um.consultar_saldo()