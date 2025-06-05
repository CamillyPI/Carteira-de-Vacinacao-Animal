class Animal:
        
    def __init__(self, nome, idade, especie, raca, id=None):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.raca = raca


    def __str__(self):
        return (f"{self.nome} ({self.raca}, {self.especie})")