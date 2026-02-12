import oracledb

class OracleEnfermos:
    # Declarar las propiedades en el constructor.
    def __init__(self):
        self.connection = oracledb.connect(user="system",
                              password="oracle", 
                              dsn="localhost/FREEPDB1")

    # Aqui los metodos que deseemos.
    # Cada metodo tendra la norma Entrar/Salir
    def eliminarEnfermo(self, inscripcion):
        cursor = self.connection.cursor()
        sql = "delete from enfermo where inscripcion = :ins"
        cursor.execute(sql, (inscripcion,))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    
