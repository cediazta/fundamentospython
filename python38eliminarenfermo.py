# Mostrar apellido e inscripcion de todos los enfermos.
# Eliminar un enfermo por su inscripcion.


import oracledb

# Conectamos con la BBDD
connection = oracledb.connect(user="system", 
                              password="oracle", 
                              dsn="localhost/FREEPDB1")

# Consulta 1 (Mostrar apellido e inscripcion de enfermos)
cursor = connection.cursor()
sql = "select apellido, inscripcion from enfermo"
cursor.execute(sql)
for row in cursor:
    print(f"{row[0]}, Inscripcion: {row[1]}")

# Consulta 2 (Eliminar un enfermo por su inscripcion)
idEnfermo = input("Indica el id del enfermo: ")
sql = "delete from ENFERMO where INSCRIPCION=" + idEnfermo
cursor.execute(sql)
afectados = cursor.rowcount
print(f"Registros eliminados:{afectados}")

# Confirmamos y Cerramos recursos
connection.commit()
cursor.close()
connection.close()
print("Fin de programa")