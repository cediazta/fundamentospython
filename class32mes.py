
class Mes:
    def __init__(self):
        self.nombre = ""
        self.tempMin = 0
        self.tempMax = 0
    
    def getTempMedia(self):
        media = (self.tempMax + self.tempMin) / 2
        return media

