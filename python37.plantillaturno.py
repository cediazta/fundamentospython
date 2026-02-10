## Vamos a mostrar todos los apellidos y funciones de los empleados de la plantilla que tengan un turno que pediremos al usuario. 

import oracledb

connection = oracledb.connect(user="system", 
                              password="oracle", 
                              dsn="localhost/FREEPDB1")
turno = input("Danos un turno (M,T,N): ").upper()

sql = (f"select apellido, funcion from plantilla where turno='{turno}'")
print(sql)

cursor = connection.cursor()
cursor.execute(sql)

for row in cursor:
    apellido = row[0]
    funcion = row[1]
    print(f"{apellido}, {funcion}")

cursor.close()
connection.close()
print("Fin de programa.")

