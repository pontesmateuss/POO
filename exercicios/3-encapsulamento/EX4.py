class ContaBancaria:
    def __init__(self,titular):
        self.titular = titular
        self.__saldo = 0


    @property
    def get_saldo(self,):
        return self.__saldo

    @get_saldo.setter
    def set_saldo(self, valor):
        if valor > 0:
            self.__saldo =  valor
        else:
            print("Coloque um valor positivo")

    def depositar(self,valor):
        if valor <= 0:
            print("Valor de depósito Inválido")
        else:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo Inválido ou insuficiente")


conta_um = ContaBancaria("Pontes")
conta_um.depositar(1000)
conta_um.sacar(300)
print(f"Saldo atual: {conta_um.get_saldo}")
conta_um.set_saldo = 1300
print(f"Saldo atual: {conta_um.get_saldo}")