##declaração da classe

class Pessoa:
    
    """
    Classe pessoa tem nome e idade,Basta usar
    Variavel = Pessoa(nome,idade)
    """
    
    def __init__(self,nome="",idade=0):#construtor
        #instancia
        self.nome = nome
        self.idade = idade
        
    ##metodos da instancia
    def aniversario(self):
        self.idade += 1
    
    def __str__(self) : 
        return f"{self.nome} é uma pessoa ela tem {self.idade} anos"
        

##objeto

p1 = Pessoa("Gabriel",25)
p1.aniversario()
print(p1)
print(p1.__dict__)


