from class32mes import Mes

print("Trabajando con clases")
listaMeses = []
for i in range(1, 4):
    mes = Mes()
    mes.nombre = input(f"Introduzca el mes {i}: ")
    mes.tempMax = int(input("Temperatura Maxima: "))
    mes.tempMin = int(input("Temperatura Minima: "))
    listaMeses.append(mes)


for dato in listaMeses:
    print(f"\n{dato.nombre}:")
    print(f"Maxima {str(dato.tempMax)}.")
    print(f"Minima {str(dato.tempMin)}.")
    print(f"Media {dato.getTempMedia()}.")

print("Fin de programa")