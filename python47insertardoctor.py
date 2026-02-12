# Vamos a realizar un programa para insertar un Doctor.
# Los datos que vamos a pedir al doctor son los siguientes:
# Id Doctor, Apellido, Especialidad, salario.
# una vez que pedimos estos datos, mostraremos un menu con los hospitales para que el usuario seleccione a que hospital quiere llevar al doctor.

import oracledb

# Conectamos con la BBDD
connection = oracledb.connect(user="system", 
                              password="oracle", 
                              dsn="localhost/FREEPDB1")

cursor = connection.cursor()
listacodigos = []

sql = "select max(doctor_no ) + 1 as maximo from doctor"
cursor.execute(sql)
row = cursor.fetchone()
idDoctor = row[0]

apellido = input("Introduce el Apellido del Doctor: ")
especialidad = input("Introduce la Especialidad del Doctor: ").upper()
salario = int(input("Introduce el Salario del Doctor: "))
contador = 1

sql = "select nombre, hospital_cod from hospital"
cursor.execute(sql)

for row in cursor:
    print(f"{contador}. {row[0]}")
    listacodigos.append(row[1])
    contador +=1

hospital = int(input("Seleccione el hospital a añadir el doctor: "))
idHospital = listacodigos[hospital - 1]

sql = "insert into doctor values (:hospital, :iddoctor, :apellido, :especialidad, :salario)"
cursor.execute(sql, (idHospital, idDoctor, apellido, especialidad, salario,))

connection.commit()
print("Doctor insertado.")
cursor.close()
connection.close()







