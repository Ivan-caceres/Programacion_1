"""
Ingresar un mes por input e informar:
Si tiene 28 días.
Si tiene 30 días.
Si tiene 31 días. 
"""
mes_ingresado = input("Ingrese un mes: ")

match mes_ingresado:
    case "febrero":
        mensaje = "Este mes tiene 28 días."

    case "abril" | "junio" | "septiembre" | "noviembre" :
        mensaje = "Este mes tiene 30 días."

    case "enero" | "marzo" | "mayo" | "julio" | "agosto" | "octubre" | "diciembre":
        mensaje = "Este mes tiene 31 días."

    case _:
        mensaje = "El dato no correspode a un mes."

print(mensaje)
