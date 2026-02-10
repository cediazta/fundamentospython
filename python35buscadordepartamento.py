# En el siguiente ejemplo vamos a realizar un buscador de un departamento por su if.
# Pediremos al usuario que nos diga el id del dpto.


import oracledb

# Creamos conexion oracle
connection = oracledb.connect(user="system", password="oracle", dsn="localhost/FREEPDB1")

print("Conectado")

# Necesitamos una consulta para buscar un departamento
# CONSULTA DINAMICA
idDpto = input("Introduce un ID de departamento: ")

# CONSULTA ESTATICA
sql = "select * from dept where dept_no=" + idDpto
print(sql)

# Creamos un cursor
cursor = connection.cursor()

# Ejecutamos la consulta para traer los datos
cursor.execute(sql)

# Recuperamos la primera fila
row = cursor.fetchone()

#Comprobamos si tenemos datos o no en la fila
if (row == None):
    print("No existe el departamento.")
else:
    # Recuperamos los datos
    nombre = row[1] #DNOMBRE
    localidad = row[2] #LOC
    print(f"{nombre}, {localidad}")

# Liberamos los recursos
cursor.close()
connection.close()
print("Fin de programa")

