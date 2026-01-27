## METODOS
'''
# Metodos
def suma(num1, num2):
    resultado = num1 + num2
    print(f"La suma es {resultado}")

# Llamadas a metodos
num1 = int(input("Introduce primer numero: "))
num2 = int(input("Introduce segundo numero: "))
suma(num1, num2)
'''

# Con Return
# Metodos
def convertirMayusculas(texto):
    return texto.upper()

def convertirMinusculas(texto):
    return texto.lower()

def convertirMayusculaPrimera(texto):
    return texto.capitalize()

def mostrarMenu():
    print("1. Convertir en Mayusculas.")
    print("2. Convertir en Minusculas.")
    print("3. Convertir primera letra en Mayusculas.")

texto = input("Introduce un texto: ")
mostrarMenu()
valor = int(input("Que desea hacer?: "))

if valor == 1:
    print(convertirMayusculas(texto))  
elif valor == 2:
    print(convertirMinusculas(texto))
elif valor == 3:
    print(convertirMayusculaPrimera(texto))
else:
    print("Opcion erronea.")


