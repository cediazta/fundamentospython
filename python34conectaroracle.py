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
row = cursor.fetchone() #Primera fila
print(row)
row = cursor.fetchone() #Segunda fila
print(row)
row = cursor.fetchone() #Tercera fila
print(row)
row = cursor.fetchone() #Cuarta fila
print(row)

# Siempre que finalicemos las acciones, debemos liberar los recursos
cursor.close()
connection.close()
print("Fin de programa.")

