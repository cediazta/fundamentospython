class Coche:
    # Declaramos las propiedades en el constructor
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.velocidad = 0
        self.estado = False

    def arrancar(self):
        self.estado = True
        print("Coche arrancado")

    def detener(self):
        self.estado = False
        print("Coche detenido")

    def acelerar(self):
        if self.estado == False:
            print("el coche no esta arrancado, Debes arrancarlo antes.")
        else:
            self.velocidad += 20
            print(f"Velocidad actual {self.velocidad} kmh.")
    
    def frenar(self):
        if self.velocidad == 0:
            print("El coche esta detenido.")
        else:
            self.velocidad -=20
            print(f"Velocidad actual {self.velocidad} kmh.")
        