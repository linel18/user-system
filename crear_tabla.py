import sqlite3

def create_table():
    conexion = sqlite3.connect('database.sql')

    consulta = conexion.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS test(
    id INTEGER PRIMARY KEY NOT NULL,
    user VARCHAR(10) NOT NULL,
    password INTEGER NOT NULL,
    fecha DATE NOT NULL)"""

    if consulta.execute(sql):
        print("Tabla creada con exito.")
    else:
        print("Error: No se ha podido crear la tabla")

    consulta.close()
    conexion.commit()
    conexion.close()
