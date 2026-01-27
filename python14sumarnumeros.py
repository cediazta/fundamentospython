# Variables
contador = 0
suma = 0

# Bucle
while True:
    num = int(input("Introduce un numero (cero termina el programa): "))
    if num != 0:
        contador += 1
        suma += num
    else:
        print(f"Numeros introducidos: {contador}.")
        print(f"La suma de todos los numeros es: {suma}.")
        break
        
    


    