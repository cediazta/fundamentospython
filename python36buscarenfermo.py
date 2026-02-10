## BUSCAR UN ENFERMO POR SU INSCRIPCION
## pediremos la inscripcion al usuario y si existe, dibujamos sus datos (apellido y direccion) y sino indicamos que el enfermo no existe


import oracledb

connection = oracledb.connect(user="system", password="oracle", dsn="localhost/FREEPDB1")


numInscripcion = input("Indica el numero de inscripcion: ")

sql = "select apellido, direccion from enfermo where inscripcion=" + numInscripcion

cursor = connection.cursor()

cursor.execute(sql)

row = cursor.fetchone()

if (row == None):
    print("No hay ningun enfermo con ese numero de inscripcion.")
else:
    apellido = row[0]
    direccion = row[1]
    print(f"{numInscripcion} - {apellido} - {direccion}")

cursor.close()
connection.close()
print("fin de programa")