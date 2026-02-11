# Mostrar lso empleados de un departamento por su ID de departamento.
# El problema esta en que no me acuerdo de los numeros de departamento que tenemos.
# Mostrar al usuario los numeros de departamento.

import oracledb

# Conectamos con la BBDD
connection = oracledb.connect(user="system", 
                              password="oracle", 
                              dsn="localhost/FREEPDB1")

cursor = connection.cursor()
sql = "select dept_no, dnombre from dept"
cursor.execute(sql)

print("---------- Menu Departamentos -----------")
for row in cursor:
    print(f"Departamento: {row[0]}, Nombre: {row[1]}")
dpto = int(input("Introduce el numero del departamento: "))
sql = "select apellido, oficio from emp where dept_no = :parametro"
cursor.execute(sql, (dpto,))

print("\n-------------- Empleados -------------")
for row in cursor:
    print(f"Apellido: {row[0]} - Oficio: {row[1]}")

cursor.close()
connection.close()
print("Fin de programa")
           
        
