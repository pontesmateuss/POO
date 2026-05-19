class ContaCorrente:
    def __init__(self, nome_correntista, cpf_correntista, saldo):
        self.nome_correntista = nome_correntista
        self.cpf_correntista = cpf_correntista
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def mostrar_saldo(self):
        print("\n--- Informações da Conta ---")
        print(f"Nome: {self.nome_correntista}")
        print(f"CPF: {self.cpf_correntista}")
        print(f"Saldo atual: R${self.saldo:.2f}")


# Programa principal

# Inputs do usuário
nome = input("Digite o nome do correntista: ")
cpf = input("Digite o CPF do correntista: ")
saldo_inicial = float(input("Digite o saldo inicial: "))

# Criando a conta
conta = ContaCorrente(nome, cpf, saldo_inicial)

# Depósito
valor_deposito = float(input("Digite o valor para depósito: "))
conta.depositar(valor_deposito)

# Saque
valor_saque = float(input("Digite o valor para saque: "))
conta.sacar(valor_saque)

# Mostrar informações finais
conta.mostrar_saldo()