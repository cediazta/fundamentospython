# Entrada de datos
inicio = int(input("Introduzca el numero de inicio: "))
final = int(input("Introduzca el numero final: "))

# Bucle For
for i in range(inicio, final + 1):
    if (i % 2 == 0):
        print(i)

# Bucle while
while (inicio <= final):
    if (inicio % 2 == 0):
        print(inicio)
    inicio += 1



