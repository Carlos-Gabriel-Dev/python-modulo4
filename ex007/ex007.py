class Livro:

    def __init__(self, titulo='', pagina=0):
        self.titulo = titulo
        self.pagina = pagina
        self.pagina_atual = 0

    def avancar_pagina(self):
        if self.pagina_atual < self.pagina:
            self.pagina_atual += 1

        return f'Você está na página {self.pagina_atual}'

    def voltar_pagina(self):
        if self.pagina_atual > 0:
            self.pagina_atual -= 1

        return f'Você está na página {self.pagina_atual}'


l1 = Livro('acf', 3000)

print(l1.avancar_pagina())