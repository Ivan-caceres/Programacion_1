"""
Ingresar un mes por input e informar por consola:
Si estamos en Invierno: "Abrigate que hace frio."
Si aún no llego el Invierno: "Falta para el invierno."
Si ya paso el Invierno: "Ya pasamos el frio, ahora calor!"
Aclaración: Se debe tomar a Julio y Agosto como los meses de invierno. 
"""

mes_ingresado = input("Ingrese un mes: ")

match mes_ingresado:
    case "julio" | "agosto":
        mensaje = "Abrigate que hace frio."
    
    case "septiembre" | "octubre" | "noviembre" | "diciembre":
        mensaje = "Ya pasamos el frio, ahora calor!"

    case "enero" | "febrero" | "marzo" | "abril" | "mayo" | "junio": 
        mensaje = "Falta para el invierno."
    
    case _:
        mensaje = "El dato no correspode a un mes."

print(mensaje)