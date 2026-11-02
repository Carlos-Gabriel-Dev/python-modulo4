class ContaBancaria : 

    def __init__(self,id, nome="", saldo = 0):
        self.nome = nome
        self.saldo = saldo
        self.id = id
        
    def __str__ (self):
        return f"O Cliente {self.nome} tem numero da conta {self.id} o saldo no valor de {self.saldo}"
        
    def deposito (self,valor): 
        self.saldo += valor
        return f'O deposito no valor de {valor} foi realizado com sucesso ,feito pela conta {self.id}'
        
    def saque (self,valor):
        if valor > self.saldo : 
            print(f"Saque negado de R${valor} na conta {self.id}")
            
        else : 
            self.saldo -= valor
            print(f'O Saque no valor de R${valor:.2f} autorizado na conta {self.id}')
        
        
        
cliente1 = ContaBancaria(123,'Gabriel',1001)

cliente1.saque(3000)
