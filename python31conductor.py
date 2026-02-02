from class31coche import Coche
from class31deportivo import Deportivo

print("Conduciendo...")

depor = Deportivo()
depor.arrancar()
depor.acelerar()
depor.turbo()

car = Coche()
car.marca = "Ford"
car.modelo = "Fiesta"
print(f"{car.marca} {car.modelo}")

while True:
    print("Menu de Conduccion:")
    print("0.Salir")
    print("1.Arrancar")
    print("2.Detener")
    print("3.Acelerar")
    print("4.Detener")
    opcion = int(input("elige una opcion: "))

    if opcion == 1:
        car.arrancar()
    elif opcion == 2:
        car.detener()
    elif opcion == 3:
        car.acelerar()
    elif opcion == 4:
        car.frenar()
    elif opcion == 0:
        break
    else:
        print("Has seleccionado una opcion erronea.")
