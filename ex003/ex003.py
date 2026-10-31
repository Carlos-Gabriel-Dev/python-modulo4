class ContaBancaria : 

    def __init__(self,id, nome="", saldo = 0):
        self.nome = nome
        self.saldo = saldo
        self.id = id
        
    def __str__ (self):
        return f"O Cliente {self.nome} tem numero da conta {self.id} o saldo no valor de {self.saldo}"
        
        
        
cliente1 = ContaBancaria(123,'Gabriel',1000)

print(cliente1)