from class31coche import Coche

class Deportivo(Coche):
    def turbo(self):
        self.velocidad += 100
        print(f"Tubo actiavdo! {self.velocidad} kmh.")

    def acelerar(self):
        self.velocidad += 45
        print("")
    
