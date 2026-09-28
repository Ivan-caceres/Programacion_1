"""
Ingresar un mes por input e informar por consola:
Si es Enero: "Que comiences bien el año!"
Si es Marzo: "A clases!"
Si es Julio: "Se vienen las vacaciones!"
Si es Diciembre: "Felices fiestas!" 
"""
mes_ingresado = input("Ingrese un mes: ")

match mes_ingresado:
    case "enero":
        print("Que comiences bien el año!")
    
    case "marzo":
        print("A clases!")

    case "julio": 
        print("Se vienen las vacaciones!")
    
    case "diciembre":
        print("Felices fiestas!")
    