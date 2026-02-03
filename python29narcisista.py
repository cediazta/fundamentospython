## NUMERO NARCISISTA

# Variables
numero = input("Introduce un numero: ")
listanumeros = []
suma = 0
numero = numero

# Bucle
for i in range(len(numero)):
    num = int(numero[i])
    potencia = num ** 3
    listanumeros.append(potencia)
    suma += potencia
    
# Control de Flujo    
if suma == int(numero):
    print("Narcisista!")
else:
    print("No es narcisista.")




