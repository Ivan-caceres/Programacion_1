from funciones import *
from mensajes import *

def menu():
    print("#"*50)
    print("Bienvenido al sistema de gestion de datos.")
    print("#"*50)

    
    bandera = True
    hay_datos = False
    opcion = 0
    
    while opcion != 7:
        print(despliegue_opciones)
        print("#"*50)

        opcion = opciones(1,7)
        if opcion == 1:
            realizar_carga()
            hay_datos = True
        elif opcion == 7:
            print("Saliendo...")
            bandera = False
        if hay_datos:
            match opcion:
                case 2: 
                    mostrar_datos()
                case 3:
                    calcular_promedio()
                case 4:
                    orden = pedir_str(
                    "Ingrese el orden [ASC/DES]: ", "ALFA")

                    mostrar_datos_ord(orden)
                case 5:
                    mostrar_mayor_prom()
                case 6:
                    legajo = pedir_str(
                    "Ingrese el numero de legajo: ", "NUM")

                    buscar_estudiantes_legajo(legajo)
        else:
            print("Error, debe cargar los datos en la opcion 1.")
