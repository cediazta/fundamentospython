import oracledb

# Conectamos con la BBDD
connection = oracledb.connect(user="system", 
                              password="oracle", 
                              dsn="localhost/FREEPDB1")

cursor = connection.cursor()

# Necesitamos una lista de oficios
listaOficios = []

# Contador
contador = 1

sql = "select distinct oficio from emp"
cursor.execute(sql)

for row in cursor:
    listaOficios.append(row[0])

# Recorremos la lista para nuestro menu
for ofi in listaOficios:
    print(f"{contador}.{ofi}")
    contador += 1

opcion = int(input("Seleccione una opcion: "))
oficioSeleccionado = listaOficios[opcion - 1]
print(f"Oficio Seleccionado: {oficioSeleccionado}")

sql = "select * from emp where oficio=:oficio"
cursor.execute(sql, (oficioSeleccionado,))

for row in cursor:
    print(f"- {row[1]}")

cursor.close()
connection.close()    
print("Fin de programa")
