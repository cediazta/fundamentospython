# mostrar los daros de empleados de un departamento, pediremos al usuario el numero de departamento.

import oracledb

# Conectamos con la BBDD
connection = oracledb.connect(user="system", 
                              password="oracle", 
                              dsn="localhost/FREEPDB1")

cursor = connection.cursor()
numero = int(input("Introduce numero de departamento: "))

sql = "select apellido, oficio, dept_no from emp where dept_no = :parametro"

cursor.execute(sql, (numero,))

for apellido, oficio, dept in cursor:
    print(f"Apellido: {apellido} - Oficio: {oficio} - Departamento: {dept}")

cursor.close()
connection.close()
print("fin de programa")

