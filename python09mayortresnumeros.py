# Entrada de datos y variables
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce le tercer numero: "))
mayor = 0
menor = 0
intermedio = 0

# Control de flujo (numero mayor)
if num1 > num2 and num1 > num3:
    mayor = num1
    if num2 > num3:
        menor = num3
        intermedio = num2
    else:
        menor = num2
        intermedio = num3
elif num2 > num1 and num2 > num3:
    mayor = num2
    if num1 > num3:
        menor = num3
        intermedio = num1
    else:
        menor = num1
        intermedio = num3
elif num3 > num1 and num3 > num2:
    mayor = num3
    if num1 > num2:
        menor = num2
        intermedio = num1
    else:
        menor = num1
        intermedio = num2

# Impresion por pantalla
print(f"El numero mayor es {mayor}")
print(f"El numero intermedio es {intermedio}")
print(f"El numero menor es {menor}")
    
    
