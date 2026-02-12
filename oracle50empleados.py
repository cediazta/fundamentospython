import oracledb

class oracleEmpleados():
    def __init__(self):
        self.connection = oracledb.connect(user="system",
                              password="oracle", 
                              dsn="localhost/FREEPDB1")
        
    def mostrarEmpleados(self):
        cursor = self.connection.cursor()
        sql = "select emp_no, apellido from EMP"
        cursor.execute(sql)
        for row in cursor:
            print(f"Empleado Num: {row[0]} - Apellido: {row[1]} ")
        cursor.close()

    def eliminarEmpleado(self, id):
        cursor = self.connection.cursor()
        sql = "delete from emp where emp_no = :id"
        cursor.execute(sql, (id,))
        registro = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registro