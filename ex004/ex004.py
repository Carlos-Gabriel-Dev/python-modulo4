from rich import print

class Funcionario:

    """Crie a classe Funcionario, na qual será possível cadastrar o nome, o setor e o cargo do funcionário. Crie também um método que permita ao funcionário se apresentar."""
    
    empresa = "Curso em Video"

    def __init__(self, nome='', setor='', cargo=''):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def saudacao (self):
        return f":handsake: Olá!, eu sou [blue]{self.nome}[/blue], sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}."

f1 = Funcionario('Gabriel', 'T.I', 'Analista')

print(f1.saudacao())