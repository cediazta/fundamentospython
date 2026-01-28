## CALCULADORA
# Funciones
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

def menuOpciones():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

# Muestra por pantalla
print("----- CALCULADORA -----")

# Entrada de datos y Variables
while True:
    num1 = int(input("Introduzca el primer numero: "))
    num2 = int(input("Introduzca el segundo numero: "))
    menuOpciones()
    opcion = int(input("Que operacion desea realizar: "))
    resultado = 0

    # Control de flujo de Calculos
    if opcion == 1:
        resultado = sumar(num1, num2)
        print(f"El resultado de la suma es {resultado}")
        respuesta = input("¿Quieres hacer mas operaciones?(Y/N): ").lower()
        if respuesta == "n":
            break
    elif opcion == 2:
        resultado = restar(num1, num2)
        print(f"El resultado de la resta es {resultado}")
        respuesta = input("¿Quieres hacer mas operaciones?(Y/N): ").lower()
        if respuesta == "n":
            break
    elif opcion == 3:
        resultado = multiplicar(num1, num2)
        print(f"El resultado de la multiplicacion es {resultado}")
        respuesta = input("¿Quieres hacer mas operaciones?(Y/N): ").lower()
        if respuesta == "n":
            break
    elif opcion == 4:
        resultado = dividir(num1, num2)
        print(f"El resultado de la division es {resultado}")
        respuesta = input("¿Quieres hacer mas operaciones?(Y/N): ").lower()
        if respuesta == "n":
            break

