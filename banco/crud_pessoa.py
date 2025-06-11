from banco.conexao import conectando
from moldes.Pessoa import Pessoa
 
def inserir_pessoa(pessoa: Pessoa) -> int:
    conn = conectando()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO Pessoa (nome, email, senha)
                   VALUES (?,?,?)""", (pessoa.nome, pessoa.email, pessoa.senha))
    
    conn.commit()
    pessoa_id = cursor.lastrowid
    conn.close()
    return pessoa_id


def alterar_pessoa(pessoa: Pessoa) -> int:
    conn = conectando()
    cursor = conn.cursor()

    cursor.execute("""UPDATE Pessoa SET nome = ?, email = ?, senha = ? WHERE id = ?""", 
                   (pessoa.nome, pessoa.email, pessoa.senha, pessoa.id))
    
    conn.commit()
    conn.close()
    return pessoa.id


def listar_pessoas():
    conn = conectando()
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM Pessoa""")
    resultado = cursor.fetchall()

    conn.close()
    return resultado


def deletar_pessoa(pessoa_id: int):
    conn = conectando()
    cursor = conn.cursor()

    cursor.execute("""DELETE FROM Pessoa WHERE id = ?""", (pessoa_id,))

    conn.commit()
    conn.close()