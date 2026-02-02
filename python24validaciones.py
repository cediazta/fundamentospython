# Libreria
from libreria24validaciones import *

# Muestra por pantalla
menuOpciones()
opcion = int(input("Que desea validar: "))

if opcion == 1:
    print("---- Validacion de ISBN ----")
    isbn()

if opcion == 2:
    print("---- Validacion de Letra DNI ----")
    letraDni()

if opcion == 3:
    print("---- Validacion DNI ----")
    dni()
    
# TERMINAR EN CASA