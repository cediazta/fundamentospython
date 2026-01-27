# STRINGS
texto = "primero pYthon"

# METODOS DE STRINGS
print(f"upper: {texto.upper()}")
print(f"lower: {texto.lower()}")
print(f"replace: {texto.replace("o", "@")}")
print(f"letra 0: {texto[0]}")
print(f"longitud: {len(texto)}")
print(f"find(p): {texto.find("p")}")
print(f"find(z): {texto.find("z")}")

# SOBRECARGA DE UN METODO
print(f"find(p, index): {texto.find("p", 0)}")
print(f"rfind(p): {texto.rfind("p")}")
print(f"startswith(a): {texto.startswith("a")}")
print(f"endwith(n: {texto.endswith("n")})")
print(f"isdigit(): {texto.isdigit()}")
print(f"isalpha(): {texto.isalpha()}")
print(f"isalnum(): {texto.isalnum()}")

# SLICING (Substring) 
# recuperar una parte de un texto
subcadena = texto[2: ]
print(f"texto[2:]: {subcadena}")

# Recuperar desde una posicion hasta otra posicion
subcadena = texto[2:5]
print(f"texto[2:5]: {subcadena}")

# Recorrer cada caracter con un bucle
longitud = len(texto)
for i in range(longitud):
    letra = texto[i]
    print(f"letra[{str(i)}] = {letra}")

# Validar lo que nos ofrece el usuario
dato = input("Introduce un numero: ")
if (dato.isdigit() == True):
    print("Me has dado un numero.")
else:
    print("Que me des un numero!!!")

