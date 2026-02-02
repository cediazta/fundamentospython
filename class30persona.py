class Persona:
    # DECLARACION DE PROPIEDADES
    nombre = ""
    apellidos = ""
    pais = ""
    email = ""
    anyoNacimiento = 0

    # CONSTRUCTOR
    def __init__(self):
        self.pais = "Francia"
        
    def __str__ (self):
            return "hoy es lunes."
    
    # METODOS
    def getNombreCompleto(self):
        return self.nombre + " " + self.apellidos

    def getEdad(self):
        return 2026 - self.anyoNacimiento
    
    def getEdadFalsa(self, anyosquitados):
         return 2026 - self.anyoNacimiento - anyosquitados
         

        
