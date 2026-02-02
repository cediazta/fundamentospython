from class30persona import Persona
print("Manejando clases persona")
# Creamos una persona
persona1 = Persona()
persona1.nombre = "Cesar"
persona1.apellidos = "Diaz Tardon"
persona1.anyoNacimiento = 1987
persona1.email = "cdiazt.1987@gmail.com"
persona1.pais = "España"
print(persona1.getNombreCompleto())
print(f"Edad {persona1.nombre}: {persona1.getEdad()}")

persona2 = Persona()
print(f"Persona pais {persona2.pais}")
print(persona2)
print ("Fin de programa")




