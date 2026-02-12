# Quiero un menu con las funciones de la plantilla.
# El usuario seleccionara una funcion, ilustraremos los apellidos de los empleados de la funcion seleccionada.

import oracledb

# Conectamos con la BBDD
connection = oracledb.connect(user="system", 
                              password="oracle", 
                              dsn="localhost/FREEPDB1")

cursor = connection.cursor()
