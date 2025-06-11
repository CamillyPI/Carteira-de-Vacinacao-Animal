from conexao import conectando
from moldes.Animal import Animal
 
def inserir_animal(animal: Animal) -> int:
    conn = conectando()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO Animal (nome, idade, especie, raca, pessoa_id)
                   VALUES (?,?,?,?,?)""", (animal.nome, animal.idade, animal.especie, 
                                           animal.raca, animal.pessoa_id))
    
    conn.commit()
    animal_id = cursor.lastrowid
    conn.close()
    return animal_id


def alterar_animal(animal: Animal) -> int:
    conn = conectando()
    cursor = conn.cursor()

    cursor.execute("""UPDATE Animal SET nome = ?, idade = ?, especie = ?, raca = ?, 
                   pessoa_id = ? WHERE id = ?""", 
                   (animal.nome, animal.idade, animal.especie, 
                    animal.raca, animal.pessoa_id, animal.id))
    
    conn.commit()
    conn.close()
    return animal.id


def listar_animais():
    conn = conectando()
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM Animal""")
    resultado = cursor.fetchall()

    conn.close()
    return resultado


def deletar_animal(animal_id: int):
    conn = conectando()
    cursor = conn.cursor()

    cursor.execute("""DELETE FROM Animal WHERE id = ?""", (animal_id,))

    conn.commit()
    conn.close()