# Entrada de datos y variables
horas = int(input("INTRODUZCA HORAS SEMANALES:\n"))
importe_hora = int(input("INTRODUZCA IMPORTE HORA:\n"))
km = int(input("INTRODUZCA KILOMETROS:\n"))
horas_extras = 0
importe_extra = 0
destino = "0"
retencion = 0
iva_salario = 0
salario_neto = 0
horas_extras = horas - 36

# Control de flujo horas extras
if horas > 36:
    importe_extra = (horas_extras * 1.5) * importe_hora

# Operaciones salario base y salario total
salario_base = (horas - horas_extras) * importe_hora
salario_total = salario_base + importe_extra

# Control de flujo destino
if km >= 101 and km <= 900:
    destino = "NACIONAL"
elif km > 900:
    destino = "INTERNACIONAL"
else:
    destino = "PROVINCIAL"

# Control de flujo retencion
if salario_total <= 250:
    retencion = 0
elif salario_total > 250 and salario_total<= 500:
    retencion = 20
else:
    retencion = 50

# Operaciones calculo de iva
iva_salario = salario_total * 0.16
salario_neto = salario_total - iva_salario

# Muestra por pantalla
print("------------------------")
print("    *** REPORTE ***     ")
print("------------------------")
print(f"HORAS TRABAJADAS: {horas}")
print(f"HORAS EXTRAS: {horas_extras}")
print(f"IMPORTE DE LA HORA: {importe_hora}")
print(f"DISTANCIA EN KM: {km}")
print(f"DESTINO: {destino}")
print(f"RETENCION: {retencion}%")
print(f"SALARIO BASE: {round(salario_base, 2)}")
print(f"SALARIO HORAS EXTRAS: {round(importe_extra, 2)}")
print(f"SALARIO BRUTO: {round(salario_total, 2)}")
print(f"IVA(16%): {round(iva_salario, 2)}")
print("------------------------")
print(f"SALARIO TOTAL: {round(salario_neto, 2)}")
print("------------------------")
print("FIN DE PROGRAMA")
    


