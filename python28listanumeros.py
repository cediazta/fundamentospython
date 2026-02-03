## LISTA NUMEROS

# Variables
numero = 0
suma = 0
sumaPares = 0
sumaImpares = 0
listaNumeros = []
listaPares = []
listaImpares = []

# Bucle
while True:
    num = int(input("Introduzca numeros, (para terminar escriba -1): "))
    if num != -1:
        listaNumeros.append(num)
        suma += num
        if num % 2 == 0:
            listaPares.append(num)
            sumaPares += num
        else:
            listaImpares.append(num)  
            sumaImpares += num
    else:
        break
    

# Mostrar por Pantalla
print(f"La suma total de los numeros es {suma}.")
print(f"Numeros introducidos:  {len(listaNumeros)}")
print(f"Numeros pares: {len(listaPares)}")
print(f"Numeros impares: {len(listaImpares)}")
print(f"Suma pares: {sumaPares}")
print(f"Suma impares: {sumaImpares}")


