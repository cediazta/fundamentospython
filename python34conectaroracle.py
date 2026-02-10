import oracledb

print("Conectando a Oracle")
# Tenemos un objeto connection que nos pedira:
# (user, password y server)
connection = oracledb.connect(user="system", password="oracle", dsn="localhost/FREEPDB1")
print("Estamos conectados!!")

# La consulta SQL desde python no finaliza;
sql = "select * from DEPT"

# Las consultas select se ejecutan a partir de connection y se crea un objeto llamado cursor.
cursor = connection.cursor()

# Una vez que tenemos el cursor, ejecutamos la consulta para que nos devuelva los datos de oracle
cursor.execute(sql)

# Aqui ya estan los datos
# Una vez tenemos el cursor, debemos leer los datos.
# Tenemos un metodo llamado fetchone() que se mueve una fila cada vez que lo ejecutamos.
# Nos devuelve la fila en la que estamos posicionados.
# Comentarios en bloque Vs code
# Seleccionamos lo que deseemos comentar (APUNTES)


'''
row = cursor.fetchone() #Primera fila
print(row)
row = cursor.fetchone() #Segunda fila
print(row)
row = cursor.fetchone() #Tercera fila
print(row)
row = cursor.fetchone() #Cuarta fila
print(row)
'''
# Si queremos leer todos los regstros del cursor:
# 1 - While
'''
row = cursor.fetchone()
while (cursor.fetchone() != None):
    print("Leer filas..")
    row = cursor.fetchone()
'''
# 2 - For
'''
for row in cursor:
    print(row)
    # Tambien podemos extraer los datos de alguna columna mediante su indice.
    print(row[0]) #DEPT_NO
    print(row[1]) #DNOMBRE
    # En algunas BBDD nos permite extraer el dato de la fila por el nombre de la columna, pero oracle no lo permite
    nombre = row.DNOMBRE
    print(nombre) '''

# 3 - Recorrer con variables el cursor
# nuestra consulta tiene 3 columnas
for numero, nombre, localidad in cursor:
    # luego decidimos cual mostrar por pantalla
    print(nombre)


# Siempre que finalicemos las acciones, debemos liberar los recursos
cursor.close()
connection.close()
print("Fin de programa.")

