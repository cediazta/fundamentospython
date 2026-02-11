# Realizar una practica en la que incrementaremos el salario de los empleados por un oficio.
# Pediremos el oficio y el incremento al usuario.
# Una vez incrementado, mostraremos el numero de empleados que han sido incrementados (7 empleados) y tambien los datos de los empleados del oficio (apellido y salario).

import oracledb

# Conectamos con la BBDD
connection = oracledb.connect(user="system", 
                              password="oracle", 
                              dsn="localhost/FREEPDB1")

cursor = connection.cursor()

oficioUsu = input("Indica el oficio: ").upper()
salarioUsu = int(input("Introduzca la subida de salario: "))

sql = "update emp set salario = salario + :parametro1 where oficio = :parametro2"

cursor.execute(sql, (salarioUsu, oficioUsu,))
registros = cursor.rowcount
connection.commit()
print(f"Personas afectadas: {registros}")

sql = "select * from emp where oficio =:inventado"
cursor.execute(sql, (oficioUsu,))

for row in cursor:
    print(f"Apellido: {row[1]} - Oficio: {row[2]} - Salario: {row[5]}")

cursor.close()
connection.close()

print("fin de programa")