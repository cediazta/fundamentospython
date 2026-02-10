# Insertar de Dept los valores (88, 'NUEVO', 'NUEVO')


import oracledb

# Conectamos con la BBDD
connection = oracledb.connect(user="system", 
                              password="oracle", 
                              dsn="localhost/FREEPDB1")
cursor = connection.cursor()

print("conectado")

id = input("ID departamento: ")
nombre = input("Nombre departamento: ")
localidad = input("Localidad: ")

# insert into dept values(88, 'NUEVO', 'NUEVO')
sql = f"insert into dept values({id}, '{nombre}', '{localidad}')"
cursor.execute(sql)
connection.commit()

sql = "select * from DEPT"
cursor.execute(sql)

for row in cursor:
    num = row[0]
    nom = row[1]
    loc = row[2]
    print(f"Id: {num}, Nombre: {nom}, Localidad: {loc}")

cursor.close()
connection.close()
print("Fin de programa.")