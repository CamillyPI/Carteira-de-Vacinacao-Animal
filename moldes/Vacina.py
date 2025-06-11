class Vacina:
        
    def __init__(self, nome, dose, data, animal_id, id=None):
        self.id = id
        self.nome = nome
        self.dose = dose
        self.data = data
        self.animal_id = animal_id


    def __str__(self):
        return (f"{self.nome} - {self.dose} - {self.data}")