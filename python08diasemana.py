# Titulo
print("** Calculo del dia de la semana segun tu nacimiento **")

# Entrada de datos
dia = int(input("Indica el numero del dia de tu nacimiento: "))
mes = int(input("Indica el numero del mes de tu nacimiento: "))
anyo = int(input("Indica el numero del año de tu nacimiento: "))

# Control de flujo (Enero/Febrero)
if mes == 1:
    mes += 12
    anyo -= 1
elif mes == 2:
    mes += 12
    anyo -= 1

# Operaciones
ope1 = int(((mes + 1) * 3) / 5)  
ope2 = int(anyo / 4)              
ope3 = int(anyo / 100)            
ope4 = int(anyo / 400)            
ope5 = int(dia + (mes * 2) + anyo + ope1 + ope2 - ope3 + ope4 + 2)
ope6 = int(ope5 / 7)
ope7 = int(ope5 - (ope6 * 7))

# Control de flujo (Dias de la Semana)
if ope7 == 0:
    print("Naciste un Sabado.")
elif ope7 == 1:
    print("Naciste un Domingo.")
elif ope7 == 2:
    print("Naciste un Lunes.")
elif ope7 == 3:
    print("Naciste un Martes.")
elif ope7 == 4:
    print("Naciste un Miercoles.")
elif ope7 == 5:
    print("Naciste un Jueves.")
elif ope7 == 6:
    print("Naciste un Viernes.")




