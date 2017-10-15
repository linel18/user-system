import sqlite3, datetime
import random

def register_user():
    conexion = sqlite3.connect('database.sql')
    consulta = conexion.cursor()

    digitos = False
    letras = False
    registro = False
    

    while registro == True:
        user = str(input("Introduzca un usuario: "))
        passw = input("Introduzca la contraseña: ")

        for i in passw:
            if i.isdigit():
                digitos = True
            if i.isalpha():
                letras = True
        if digitos == False:
            print("Error la contraseña debe contener numeros")
        if letras == False:
            print("Error la contraseña debe contener letras")

        else:
            registro = True
        
    user1 = user        
    

    id1 = random.randint(1000, 10000)

    sql1 = "SELECT * FROM test WHERE user = \"%s\"" % user1

    if consulta.execute(sql1):
        try:
            filas = consulta.fetchone()
            print("El usuario %s ya se encuentra registrado" % filas[1])

        except TypeError:
            argumentos = (id1, user, passw, datetime.date.today())

            sql = """INSERT INTO test(id, user, password, fecha)
            VALUES (?, ?, ?, ?)"""

            if consulta.execute(sql, argumentos):
                print("Registro creado con exito. id de usuario: %s" % id1)



    consulta.close()
    conexion.commit()

    conexion.close()

