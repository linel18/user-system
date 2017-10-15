from crear_tabla import create_table
from registro import register_user
import os.path as path
import sqlite3


conexion = sqlite3.connect('database.sql')
intens_logins = 0

if not path.exists('database.sql'):
    create_table()



while True:
        while intents_logins < 3:
            global intents_logins
            user = input("Introduzca su usuario: ")
            passw = int(input("Introduzca su contraseña: "))

            database = conexion.cursor()


            sql = "SELECT * FROM test WHERE user = \"%s\"" % user


            if database.execute(sql):
                fila = database.fetchone()

                try:
                    if fila[2] == passw:
                        print("Contraseña aceptada.")

                        print("informacion de usuario")
                        print("""id         usuario       fecha de registro

%s       %s         %s
                                """ % (fila[0], fila[1], fila[3]))
                        break
                    else:
                        print("Contraseña incorrecta.")
                        intents_logins += 1
                except TypeError:
                    print('Error usuario no registrado')
                    intents_logins += 1
                    continue


        






database.close()

conexion.close()
          
