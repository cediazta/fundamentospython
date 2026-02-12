# Quiero una aplicacion que se encargara de eliminar empleados por su ID.

from oracle50empleados import oracleEmpleados

print("---------- EMPLEADOS -----------")
mostrar = oracleEmpleados()
mostrar.mostrarEmpleados()
print("--------------------------------")

id = int(input("Num. Empleado a eliminar: "))
oracle = oracleEmpleados()
registro = oracle.eliminarEmpleado(id)
print(f"{registro} registro eliminado.")
