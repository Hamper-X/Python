class Serie:
    def __init__ (self, nome, ano, avaliacao):
        self.nome = nome
        self.ano = ano 
        self.avaliacao = avaliacao

    def __str__(self):
        return f'A série {self.nome} foi lançada no ano {self.ano.strip(")").strip("(")} e possui avaliação de {self.avaliacao}' 

    