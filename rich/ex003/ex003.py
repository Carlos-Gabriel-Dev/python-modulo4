from rich import print
from rich.table import Table

tabela = Table(title=("TAbela de Preços"))

tabela.add_column("Nome")
tabela.add_column("Preço")

tabela.add_row("Lapis","R$1.60")
tabela.add_row("Borracha","R$3.00")

print(tabela)