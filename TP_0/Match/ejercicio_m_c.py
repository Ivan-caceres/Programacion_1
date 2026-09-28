"""
Ingresar un mes por input e informar:
Si es Febrero: " Este mes no tiene más de 29 días."
Si no es Febrero: "Este mes tiene 30 o más días."
"""
mes_ingresado = input("Ingrese un mes: ")

match mes_ingresado:
    case "febrero":
        mensaje = "Este mes no tiene más de 29 días."

    case "enero" | "marzo" | "abril" | "mayo" | "junio" | "julio" | "agosto" | "septiembre" | "octubre" | "noviembre" | "diciembre":
        mensaje = "Este mes tiene 30 o más días."

    case _:
        mensaje = "El dato no correspode a un mes."

print(mensaje)
