class Mascotas:
    def __init__(self):
        self.nombre = ""
        self.tipo = ""
        self.anyoNacimiento = 0
        self.anyoAdopcion = 0
    
    def getAnyosAdoptada(self):
        anyosAdoptada = 2025 - self.anyoAdopcion
        return anyosAdoptada