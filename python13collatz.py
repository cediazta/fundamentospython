# CONJETURA DE COLLATZ

# Variable
numero = int(input("Introduce un numero: "))

# Bucle while
while (numero != 1):
    if (numero % 2 == 0):
        numero = int(numero / 2)
    else:
        numero = int(numero * 3 + 1)
    print(numero)





        

