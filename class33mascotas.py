class Mascotas:
    def __init__(self):
        self.nombre = ""
        self.raza = ""
        self.anyoNacimiento = 0
        self.anyoAdopcion = 0
    
    def getAnyosAdoptada(self):
        anyosAdoptada = self.anyoAdopcion - self.anyoNacimiento
        return anyosAdoptada