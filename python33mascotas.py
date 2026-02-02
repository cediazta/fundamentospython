from class33mascotas import Mascotas

print("Informacion de mascotas:")
animales = []

for i in range (1,2):
    animal = Mascotas()
    animal.nombre = input("Introduce el nombre de la mascota: ")
    animal.raza = input("Introduce la raza del animal: ")
    animal.anyoNacimiento = int(input("Introduce el año de nacimiento: "))
    animal.anyoAdopcion = int(input("Introduzca el año de adopcion: "))
    animales.append(animal)

for dato in animales:
    print(f"\nNombre: {animal.nombre}.")
    print(f"Raza: {animal.raza}")
    print(f"Año de nacimiento: {animal.anyoNacimiento}")
    print(f"Anyo de adopcion: {animal.anyoAdopcion}")
    print(f"Años adoptada: {dato.getAnyosAdoptada()}")


