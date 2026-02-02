from class32mes import Mes

print("Trabajando con clases")
enero = Mes()
enero.nombre = "Enero"
enero.tempMin = -2
enero.tempMax = 9
print(f"Media Enero {enero.getTempMedia()} grados.")

febrero = Mes()
febrero.nombre = "Febrero"
febrero.tempMin = 5
febrero.tempMax = 15
print(f"Media Febrero {febrero.getTempMedia()} grados.")