## COMPROBACION DE EMAIL
# Variables
correo = input("Introduce un correo: ")
dominio = correo[correo.rfind("."):]
punto = correo[correo.find("@")]

# Controles de flujo
if correo.find("@") == -1:
    print("A tu correo le falta la @.")

if correo.find(".") == -1:
    print("A tu correo le falta un punto.")

if correo.startswith("@") == True:
    print("Tu correo no puede empezar por @.")

if correo.endswith("@") == True:
    print("Tu correo no puede terminar por @.")

if correo.count("@") > 1:
    print("Tu correo no puede contener mas de un @.")

if punto.find("@") > punto.find("."):
    print("El punto debe de ir despues de la @.")

if len(dominio) < 4:
    print("El dominio no puede se mas de 3 letras.")
elif len(dominio) > 3:
    print("El dominio tiene que tener minimo 2 letras.")


