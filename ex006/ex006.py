
from rich import print
from rich.panel import Panel

class Churrasco:

    consumo_padrao = 0.400
    preco_kg = 82.40

    def __init__(self, titulo='', quanti=0):

        self.titulo = titulo
        self.quanti = quanti

    def __str__(self):
        return f'Esse é {self.titulo} com {self.quanti} pessoas participando'

    def calculo_qtd_carne(self):
        return self.quanti * Churrasco.consumo_padrao

    def calculo_custo_total(self):
        return self.calculo_qtd_carne() * Churrasco.preco_kg

    def analisar(self):

        conteudo = f'Analisando {self.titulo} com {self.quanti} convidados\n\n'

        conteudo += f'Cada participante comerá {Churrasco.consumo_padrao:.3f} Kg\n'

        conteudo += f'Cada Kg de carne custa R$ {Churrasco.preco_kg:.2f}\n\n'

        conteudo += f'Recomendo comprar {self.calculo_qtd_carne():.3f} Kg de carne\n'

        conteudo += f'Custo total: R$ {self.calculo_custo_total():.2f}'

        painel = Panel(conteudo, title=self.titulo)

        print(painel)


c1 = Churrasco('Familia', 11)

c1.analisar()
