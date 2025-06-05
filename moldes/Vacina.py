class Vacina:
        
    def __init__(self, nome, dose, data, id=None):
        self.id = id
        self.nome = nome
        self.dose = dose
        self.data = data


    def __str__(self):
        return (f"{self.nome} - {self.dose} - {self.data}")