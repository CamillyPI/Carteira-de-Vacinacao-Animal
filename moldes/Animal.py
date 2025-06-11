class Animal:
        
    def __init__(self, nome, idade, especie, raca, pessoa_id, id=None):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.raca = raca
        self.pessoa_id = pessoa_id


    def __str__(self):
        return (f"{self.nome} ({self.raca}, {self.especie})")