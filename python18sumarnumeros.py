# Variables
num = input("Dame una cifra: ")
suma = 0

# Control de Fujo
if num.isdigit() == False:
    print("Lo que has puesto no son numeros")
else:
    # Bucle
    for i in range(len(num)):
        letra = num[i]
        numero = int(letra)
        suma += numero

# Mostras por pantalla
print(f"La suma de {num} es {str(suma)}.")





