"""
Ingresar un número entero que represente una hora del día e informar:
Si está entre las 7 y las 11 : "Es de mañana."
Si está entre las 12 y las 19 : "Es de tarde."
Si está entre las 20 y las 23 o entre las 0 y las 6 : "Es de noche."
Si no está entre las 0 y las 23 : "la hora no existe."

"""

hora_ingresada = int(input("Ingrese solo la hora del dia sin los minutos: "))

if 0 <= hora_ingresada <= 23:
    match hora_ingresada:
        case 7 | 8 | 9 | 10 | 11:
            print("Es de mañana.")
        case 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19:
            print("Es de tarde.")
        case _:
            print("Es de noche.")
else:
    print("La hora no existe.")
