print("Nombres en listas")
#Declarar una lista vacia
lista = []
#Entramos en un bucle infinito hasta tener
#los 5 nombres
contador = 1
while (len(lista) != 5):
    print("Dime el nombre ", contador)
    nombre = input()
    print("Nombres en lista: ", len(lista)) 
    #Debemos recorrer cada nombre dentro de nuestra lista
    if (len(lista) == 0):
        #Todavia no tenemos nombres
        lista.append(nombre)
        contador = contador + 1
    else:
        #recorremos todos los nombres
        #hasta el final, no añadimos
        existe = False
        for name in lista:
            print("Estoy en bucle")
            if (name.upper() == nombre.upper()):
                #Esta repetido
                existe = True
                #Podemos salir de un bucle a la fuerza
                #si lo deseamos
                break
        if (existe == False):
            lista.append(nombre)
            contador = contador + 1
print("---------------")
for n in lista:
    print(n)
print("Fin de programa")