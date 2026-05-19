class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome:str = nome
        self.__preco:float = preco
        self.__quantidade_em_estoque:int = quantidade
    

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            print("Valor Inválido")
        else:
            self.__preco = valor
            
    @property
    def quantidade_em_estoque(self):
        return self.__quantidade_em_estoque
    
    @quantidade_em_estoque.setter
    def quantidade_em_estoque(self, valor):
        if valor <= 0:
            print("Valor inválido")
        else:
            self.quantidade_em_estoque = valor
            
    def vender(self, quantidade):
        if 0 < self.__quantidade_em_estoque >= quantidade:
            self.__quantidade_em_estoque -= quantidade
        else:
            print("Falta de estoque!")
    def repor_estoque(self,quantidade):
        self.__quantidade_em_estoque += quantidade

    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
    def get_quantidade_em_estoque(self):
        return self.__quantidade_em_estoque
    
produto_um = Produto("Notebook Gamer RTX 9090", 7999, 999)
print(f"Produto: {produto_um.get_nome()}, Preço: R${produto_um.get_preco():.2f}, Estoque: {produto_um.get_quantidade_em_estoque()}")
produto_um.repor_estoque(1499)
produto_um.vender(999)
print(f"Estoque atual: {produto_um.get_quantidade_em_estoque()}")
produto_um.vender(1500)