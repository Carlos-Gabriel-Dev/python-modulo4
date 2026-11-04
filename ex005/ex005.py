from rich import print
from rich.panel import Panel


class Produto : 
    
    """Cria a classe Produto,onde podemos cadastrar nome e o preço.Crie um método que mostre uma etiqueta de preço do produto"""
    
    def __init__(self,nome,preco): 
        self.nome = nome
        self.preco = preco
    
    def Etiqueta (self): 
        
        etiqueta = Panel(f"{self.nome}\nR${self.preco:.2f}",title="Produto",width=30)
        print(etiqueta)
    
p1 = Produto('Borracha',1.5)
p2 = Produto("Notebook Gamer pro max",4000)

p1.Etiqueta()
p2.Etiqueta()