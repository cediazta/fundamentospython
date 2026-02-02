from class33mascotas import Mascotas

print("Informacion de mascotas:")
animales = []

for i in range(1, 3):
    animal = Mascotas()
    animal.nombre = input("Introduce el nombre de la mascota: ")
    animal.tipo = input("Introduce el tipo de animal: ")
    animal.anyoNacimiento = int(input("Introduce el año de nacimiento: "))
    animal.anyoAdopcion = int(input("Introduzca el año de adopcion: "))
    animales.append(animal)

for dato in animales:
    print(f"\nNombre: {dato.nombre}")
    print(f"Tipo: {dato.tipo}")
    print(f"Año de nacimiento: {dato.anyoNacimiento}")
    print(f"Anyo de adopcion: {dato.anyoAdopcion}")
    print(f"Años adoptada: {dato.getAnyosAdoptada()}")


