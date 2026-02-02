def menuOpciones():
    print("---- VALIDACIONES ----")
    print("1. ISBN")
    print("2. Letra DNI")
    print("3. DNI Correcto")
    print("0. Salir")

def isbn():
    contador = 1
    suma = 0
    isbn = input("Introduce el ISBN: ")
    if len(isbn) != 10:
        print("El ISBN es incorrecto, debe contener 10 digitos.")
    else:
        for i in range(len(isbn)):
            digito = isbn[i]
            numero = int(digito)
            multiplicacion = numero * contador
            contador += 1
            suma += multiplicacion       
    if suma % 11 == 0:
        print("CORRECTO")
    else:
        print("INCORRECTO")

def letraDni():
    dni = int(input("Introduce los nueve digitos de tu DNI: "))
    letra = int(dni % 23)
    if letra == 0:
        print("Tu letra es la T")
    elif letra == 1:
        print("Tu letra es la R")
    elif letra == 2:
        print("Tu letra es la W")
    elif letra == 3:
        print("Tu letra es la A")
    elif letra == 4:
        print("Tu letra es la G")
    elif letra == 5:
        print("Tu letra es la M")
    elif letra == 6:
        print("Tu letra es la Y")
    elif letra == 7:
        print("Tu letra es la F")
    elif letra == 8:
        print("Tu letra es la P")
    elif letra == 9:
        print("Tu letra es la D")
    elif letra == 10:
        print("Tu letra es la X")
    elif letra == 11:
        print("Tu letra es la B")
    elif letra == 12:
        print("Tu letra es la N")
    elif letra == 13:
        print("Tu letra es la J")
    elif letra == 14:
        print("Tu letra es la Z")
    elif letra == 15:
        print("Tu letra es la S")
    elif letra == 16:
        print("Tu letra es la Q")
    elif letra == 17:
        print("Tu letra es la V")
    elif letra == 18:
        print("Tu letra es la H")
    elif letra == 19:
        print("Tu letra es la L")
    elif letra == 20:
        print("Tu letra es la C")
    elif letra == 21:
        print("Tu letra es la K")
    elif letra == 22:
        print("Tu letra es la E")
    elif letra == 23:
        print("Tu letra es la T")

def dni():
    dniUser = input("Introduce tu dni completo: ").lower()
    dni = len(dniUser)
    numeros = dni[0:8]
    letraDni = dni[8]

    letra = int(numeros % 23)

    if letra == 0:
        print("Tu letra seria la T")
        letra == "T"
    elif letra == 1:
        print("Tu letra seria la R")
        letra == "R"
    elif letra == 2:
        print("Tu letra seria la W")
        letra == "W"
    elif letra == 3:
        print("Tu letra seria la A")
        letra == "A"
    elif letra == 4:
        print("Tu letra seria la G")
        letra == "G"
    elif letra == 5:
        print("Tu letra seria la M")
        letra == "M"
    elif letra == 6:
        print("Tu letra seria la Y")
        letra == "Y"
    elif letra == 7:
        print("Tu letra seria la F")
        letra == "F"
    elif letra == 8:
        print("Tu letra seria la P")
        letra == "P"
    elif letra == 9:
        print("Tu letra seria la D")
        letra == "D"
    elif letra == 10:
        print("Tu letra seria la X")
        letra == "X"
    elif letra == 11:
        print("Tu letra seria la B")
        letra == "B"
    elif letra == 12:
        print("Tu letra seria la N")
        letra == "N"
    elif letra == 13:
        print("Tu letra seria la J")
        letra == "J"
    elif letra == 14:
        print("Tu letra seria la Z")
        letra == "Z"
    elif letra == 15:
        print("Tu letra seria la S")
        letra == "S"
    elif letra == 16:
        print("Tu letra seria la Q")
        letra == "Q"
    elif letra == 17:
        print("Tu letra seria la V")
        letra == "V"
    elif letra == 18:
        print("Tu letra seria la H")
        letra == "H"
    elif letra == 19:

        letra == "L"
    elif letra == 20:
        letra == "C"
    elif letra == 21:
        letra == "K"
    elif letra == 22:
        letra == "E"
    elif letra == 23:
        letra == "T"

    if letra == letraDni:
        print("El DNI es CORRECTO.")
    else:
        print("El DNI es INCORRECTO.")
  
        