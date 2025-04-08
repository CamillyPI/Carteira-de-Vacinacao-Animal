import sqlite3 as conector

def criar_tabela():
    try:
        conexao = conector.connect('vacinacao_pet.db')
        cursor = conexao.cursor()

        sql_pessoa = '''CREATE TABLE if not exists Pessoa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL);
            '''

        sql_animal = '''CREATE TABLE if not exists Animal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especie TEXT NOT NULL,
            raca TEXT NOT NULL);
            '''

        sql_vacina = '''CREATE TABLE if not exists Vacina (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            dose INTEGER NOT NULL,
            data DATE NOT NULL);
            '''

        cursor.execute(sql_pessoa)
        cursor.execute(sql_animal)
        cursor.execute(sql_vacina)
        conexao.commit()
        print('Banco de dados criado!')

    except conector.DatabaseError as error:
        print(f'ERRO: {error}')

    finally:
        if conexao:
            cursor.close()
            conexao.close()