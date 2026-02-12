from oracle49enfermos import OracleEnfermos

print("Programa eliminar enfermo")
#Creamos nuestra clase de Oracle
oracle = OracleEnfermos()
print("Introduzca una inscripcion")
dato = int(input())
registros = oracle.eliminarEnfermo(dato)
print(f"Enfermos eliminados: {registros}")
print("Fin de programa")