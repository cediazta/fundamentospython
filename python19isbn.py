# Muestra por pantalla
print("------ VALIDANDO ISBN ------")

# Entrada de datos y Variables
isbn = input("Introduce el ISBN: ")
contador = 1
suma = 0

# Control de flujo digitos
if len(isbn) != 10:
    print("El ISBN es incorrecto, debe contener 10 digitos.")
else:
    # Bucle calculos
    for i in range(len(isbn)):
        digito = isbn[i]
        numero = int(digito)
        multiplicacion = numero * contador
        contador += 1
        suma += multiplicacion

# Control de flujo comprobacion Resto
if suma % 11 == 0:
    print("CORRECTO")
else:
    print("INCORRECTO")
