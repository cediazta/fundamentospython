# Entrada de datos
numero1 = int(input("Introduzca un numero: "))
numero2 = int(input("Introduzca otro numero: "))

# Controlador de flujo
if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
elif numero2 > numero1:
    print(f"{numero2} es mayor que {numero1}")
else:
    print("Ambos numeros son iguales.")
print("Fin de programa.")