# Realizar una practica para insertar una persona en la PLANTILLA.
# Pediremos al usuario el apellido, funcion, turno, salario y codigo de sala.
# mostraremos un menu con los hospitales.
import oracledb

# Conectamos con la BBDD
connection = oracledb.connect(user="system", 
                              password="oracle", 
                              dsn="localhost/FREEPDB1")

cursor = connection.cursor()

listaCodHospital = []
contador = 1
apellido = input("Introduce el Apellido: ")
funcion = input("Introdice la Funcion: ").upper()
turno = input("Introduce el Turno(M/T/N): ").upper()
salario = int(input("Introduce el Salario: "))
codSala = int(input("Introduce el Codigo de Sala: "))

sql = "select nombre, hospital_cod from hospital;"
cursor.execute(sql)

for row in cursor:
    print(f"{contador}. {row[0]}")
    listaCodHospital.append(row[1])
    contador += 1

opcion = int(input("Seleccione un hospital: "))
codHospital = listaCodHospital[opcion -1]

sql = "select max(empleado_no) + 1 as maximo from plantilla"
cursor.execute(sql)

row = cursor.fetchone()
empleadoNo = row[0]

sql = "insert into plantilla values (:hopistalcod, :salacod, :empleadoNo, :apellido, :funcion, :turno, :salario)"
cursor.execute(sql, (codHospital, codSala, empleadoNo, apellido, funcion, turno, salario,))

print("Registro añadido.")
connection.commit()
cursor.close()
connection.close()




