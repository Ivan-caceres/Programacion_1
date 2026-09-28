"""
Ingresar un numero entero que represente una hora del día e informar:
Si está entre las 7 y las 11 : "Es de mañana."
"""
hora_ingresada = int(input("Ingrese solo la hora del dia sin los minutos: "))

match hora_ingresada:
    case "7" | "8" | "9" | "10" | "11":
        print("Es de mañana.")