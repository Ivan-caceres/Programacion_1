"""
Ingresar una letra por input, validar que la misma sea „F‟ o „M‟, caso contrario
volver a pedirla. Una vez validado el ingreso de la letra, mostrar por consola:
Si la letra ingresada es „F‟: “FEMENINO”
Si la letra ingresa es „M‟: “MASCULINO”.
"""
bandera = True
while bandera:
    letra = input("Ingrese 'F' o 'M': ")
    match letra:
        case "f" | "F":
            print("FEMENINO")
            bandera = False
        case "m" | "M":
            print("MASCULINO")
            bandera = False
        case _:
            print("Opcion invalida.")