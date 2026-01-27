# Condicionales (Controlador de flujo)
    # if, elif, else
    # operadores condicionales >, <, ==, >=, <=, !=
edad = int(input("Que edad tienes?: "))

if edad > 18:
    print("Tienes mas de 18 años.")
elif edad == 18:
    print("Tienes 18 años.")
else:
    print("Tienes menos de 18 años.")

    # match, case
print("Bienvenido al Supermercado, ¿Que quiere comprar?")
compra = int(input("1.Tomates\n2.Lechugas\n3.Zanahorias: "))
             
match compra:
    case 1:
        print("Has comprado Tomates.")
    case 2:
        print("Has comprado Lechugas.")
    case 3:
        print("Has comprado Zanahorias.")