class Paciente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self._cpf = "" 
        self.cpf = cpf  
    @property
    def cpf(self) -> str:
        return self._cpf
    @cpf.setter
    def cpf(self, valor: str): 
        digitos = "".join(filter(str.isdigit, valor))        
        if len(digitos) == 11:
            self._cpf = digitos
        else:
            print(f"Erro: CPF inválido. '{valor}' não possui 11 dígitos.")
    def __str__(self):
        cpf_formatado = f"{self._cpf[:3]}.{self._cpf[3:6]}.{self._cpf[6:9]}-{self._cpf[9:]}" if len(self._cpf) == 11 else self._cpf
        return f"Paciente: {self.nome} | CPF: {cpf_formatado}"
if __name__ == "__main__":
    paciente1 = Paciente("Mateus Silva", "12345678901")
    print(paciente1)
    
    paciente1.cpf = "99999"
    print(paciente1)
