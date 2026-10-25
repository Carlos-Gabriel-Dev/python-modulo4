##declaração da classe

class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        
    ##metodos da instancia
    def aniversario(self):
        self.idade += 1
           
    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos de idade"
        

##objeto

p1 = Pessoa()

p1.nome = "Gabriel"
p1.idade = 25
p1.aniversario()

print(p1.mensagem())