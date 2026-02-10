# quiero un programa que inserte un nuevo hospital, le pedimos los datos al usuario y despues mostramos los hospitales.


import oracledb

# Conectamos con la BBDD
connection = oracledb.connect(user="system", 
                              password="oracle", 
                              dsn="localhost/FREEPDB1")
cursor = connection.cursor()

codHospital = input("Codigo del Hospital: ")
nomHospital = input("Nombre del Hospital: ")
dirHospital = input("Direccion del Hospital: ")
tlfHospital = input("Telefono del Hospital: ")
numCamasHospital= input("Numero de Camas del Hospital: ")

sql = f"insert into HOSPITAL values ({codHospital}, '{nomHospital}', '{dirHospital}', {tlfHospital}, {numCamasHospital})"
cursor.execute(sql)
connection.commit()

sql = "select * from HOSPITAL"
cursor.execute(sql)

for row in cursor:
    print(f"COD: {row[0]}, Nombre: {row[1]}, Direccion: {row[2]}, Telefono: {row[3]}, Numero de Camas: {row[4]}")

cursor.close()
connection.close()
print("Fin de programa.")






