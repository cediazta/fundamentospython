print("Diccionarios")
#Creamos el diccionario
provincias = dict()
#añadimos los elementos
provincias = {
      924 : "Badajoz"
    , 956:  "Cádiz"
    , 958 : "Granada"
    , 959 : "Huelva"
    , 91 : "Madrid"
}
#Recuperar el value de un elemento por su KEY
#Si no existe, no pasa nada, devuelve None
print(provincias.get(959))
#Recorrer cada Key, Value mediante items
for clave, valor in provincias.items():
    print("key " + str(clave) + ", Value: " + valor)
#Podemos recorrer o solo claves (keys)
#o solamente valores (values)
for clave in provincias.keys():
    print(clave) 
for valor in provincias.values():
    print(valor)
#Podemos añadir nuevos elementos key:value
provincias.setdefault(925, "Toledo")
#No podemos repetir una Key
provincias.setdefault(925, "Toledo")
#Podemos repetir el value
provincias.setdefault(933, "Toledo")
#Eliminamos un elemento por su Key
#La clave debe existir o tendremos error
provincias.pop(924)
#Eliminar toda el diccionario
provincias.clear()
print(provincias)