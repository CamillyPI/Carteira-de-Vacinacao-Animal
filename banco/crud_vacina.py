from banco.conexao import conectando
from moldes.Vacina import Vacina
 
def inserir_vacina(vacina: Vacina) -> int:
    conn = conectando()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO Vacina (nome, dose, data, animal_id)
                   VALUES (?,?,?,?)""", (vacina.nome, vacina.dose, vacina.data, 
                                           vacina.animal_id))
    
    conn.commit()
    vacina_id = cursor.lastrowid
    conn.close()
    return vacina_id


def alterar_vacina(vacina: Vacina) -> int:
    conn = conectando()
    cursor = conn.cursor()

    cursor.execute("""UPDATE Vacina SET nome = ?, dose = ?, data = ?, 
                   animal_id = ? WHERE id = ?""", 
                   (vacina.nome, vacina.dose, vacina.data, 
                    vacina.animal_id, vacina.id))
    
    conn.commit()
    conn.close()
    return vacina.id


def listar_vacinas():
    conn = conectando()
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM Vacina""")
    resultado = cursor.fetchall()

    conn.close()
    return resultado


def deletar_vacina(vacina_id: int):
    conn = conectando()
    cursor = conn.cursor()

    cursor.execute("""DELETE FROM Vacina WHERE id = ?""", (vacina_id,))

    conn.commit()
    conn.close()