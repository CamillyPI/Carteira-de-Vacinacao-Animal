import sqlite3 as connector

def conectando():
    return connector.connect('vacinacao_pet.db')

def criar_tabela():
    try:
        conexao = conectando()
        cursor = conexao.cursor()

        sql_pessoa = '''CREATE TABLE if not exists Pessoa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL)
            '''

        sql_animal = '''CREATE TABLE if not exists Animal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            especie TEXT NOT NULL,
            raca TEXT NOT NULL,
            pessoa_id INTEGER,
            FOREIGN KEY(pessoa_id) REFERENCES Pessoa(id)
            )'''

        sql_vacina = '''CREATE TABLE if not exists Vacina (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            dose INTEGER NOT NULL,
            data DATE NOT NULL,
            animal_id INTEGER
            FOREIGN KEY(animal_id) REFERENCES Animal(id)
            )'''

        cursor.execute(sql_pessoa)
        cursor.execute(sql_animal)
        cursor.execute(sql_vacina)
        conexao.commit()
        print('Banco de dados criado!')

    except connector.DatabaseError as error:
        print(f'ERRO: {error}')

    finally:
        if conexao:
            cursor.close()
            conexao.close()