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

def finalizar():
    respuesta = input("¿Quieres hacer mas operaciones?(Y/N): ").lower()
    return respuesta