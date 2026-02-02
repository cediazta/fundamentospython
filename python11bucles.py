print("Ejemplos de bucles")
print("WHILE")
#Necesitamos una variable fuera del bucle
#para nuestra condicion
contador = 0
while (contador <= 5):
    print("Contador ", contador)
    #Necesitamos cambiar el valor de "algo"
    #para salir del bucle
    contador = contador + 1
#En un bucle FOR, se declara la variable contador
#en la definicion del bucle
#Dicha variable suele llamarse i, z, k
#Hacemos un FOR de 0-5
print("FOR")
for i in range(5+1):
    print("Valor de i: ", i)
#Tenemos la posibilidad de indicar un numero de inicio y
#un numero final.  2--8
for z in range(2, 8 + 1):
    print("z: ", z)
print ("Fin de programa")