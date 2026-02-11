# Realizar un ejemplo para incrementar el salario de los empleados de la PLANTILLA de un hospital.
# Pediremos el numero de empleados afectados.
# Mostraremos el APELLIDO, SALARIO y HOSPITAL de los empleados afectados por la consulta.

import oracledb

# Conectamos con la BBDD
connection = oracledb.connect(user="system", 
                              password="oracle", 
                              dsn="localhost/FREEPDB1")

cursor = connection.cursor()
sql = "select nombre from hospital"
cursor.execute(sql)
for row in cursor:
    print(f"Hospital: {row[0]}")

hospitalUsu = input("Selecciona un hospital: ")
sql = "select hospital_cod from hospital where nombre = :parametro"
cursor.execute(sql, (hospitalUsu,))
hospitalCod = 0

for row in cursor:
    hospitalCod = row[0]

salarioUsu = int(input("Introduce el aumento de salario: "))
sql = "update plantilla set salario = salario + :parametro where hospital_cod = :parametro2" 
cursor.execute(sql, (salarioUsu, hospitalCod,))
registro = cursor.rowcount
print(f"Se han modificado {registro} registros.")

sql = "select apellido, salario from plantilla where hospital_cod = :parametro"
cursor.execute(sql, (hospitalCod,))
connection.commit()

for row in cursor:
    print(f"Apellido: {row[0]} - Salario: {row[1]} - Hospital: {hospitalUsu}")

cursor.close()
connection.close()
print("Fin de programa.")


