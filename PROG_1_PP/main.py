from funciones import *
from mensajes import *
from listas import *

def menu():
    print("#"*50)
    print("Bienvenido al sistema de gestion de datos.")
    print("#"*50)

    bandera = True
    hay_datos = True

    (legajos, nombres, generos, notas_primer_parcial, 
    notas_segundo_parcial, promedios) = listas_hardcodeadas()
    #(legajos, nombres, generos, notas_primer_parcial, 
    #    notas_segundo_parcial, promedios) = inicializar_listas()
    
    while bandera:
        print("#"*50)
        print(despliegue_opciones)
        print("#"*50)

        opcion = opciones(1,7)
        if opcion == 1:
            (legajos, nombres, generos, 
            notas_primer_parcial, notas_segundo_parcial) = realizar_carga(
            legajos, nombres, generos, notas_primer_parcial, 
            notas_segundo_parcial)
            hay_datos = True
        elif opcion == 7:
            print("Saliendo...")
            bandera = False
        elif hay_datos:
            match opcion:
                case 2: 
                    mostrar_datos(legajos, nombres, generos, 
                                notas_primer_parcial, notas_segundo_parcial)
                case 3:
                    calcular_promedio(notas_primer_parcial, 
                                    notas_segundo_parcial, promedios)
                    print("Promedio calculado, consulte opcion 5")
                    calculo_hecho = True
                case 4:
                    if calculo_hecho:
                        orden = ingresar_orden(
                        "Ingrese el orden [ASC/DES]: ")
                        (promedios, legajos, nombres, generos, 
                        notas_primer_parcial, 
                        notas_segundo_parcial) = ordenar_listas(
                        promedios, legajos, nombres, generos, 
                        notas_primer_parcial,
                        notas_segundo_parcial, orden
                        )

                        mostrar_datos(legajos, nombres, generos, 
                        notas_primer_parcial, notas_segundo_parcial, 
                        promedios)
                    else:
                        print("Error! Debe calcular promedios en opcion 3.")
                case 5:
                    if calculo_hecho:
                        indice_mayor = encontrar_mayor_prom(promedios)
                        print("#"*96)
                        print("\t\t\t\t\tESTUDIANTE CON MAYOR PROMEDIO")
                        print("#"*96)
                        print("Nro Legajo\tNombre del estudiante\t\tGenero\tNota 1er parcial\t"
                        "Nota 2do parcial\tPromedios")
                        mostrar_estudiante(legajos, nombres, generos,
                        notas_primer_parcial, notas_segundo_parcial, indice_mayor,
                        promedios)
                        print("#"*96)
                    else:
                        print("Error! Debe calcular promedios en opcion 3.")
                case 6:
                    legajo = ingresar_num("Ingrese el numero de legajo: ")

                    indice = buscar_estudiantes_legajo(legajos, legajo)
                    if indice != None:
                        print("#"*96)
                        print("\t\t\t\t\tESTUDIANTE ENCONTRADO")
                        print("#"*96)
                        print("Nro Legajo\tNombre del estudiante\t\tGenero\tNota 1er parcial\t"
                        "Nota 2do parcial\tPromedios")
                        mostrar_estudiante(legajos, nombres, generos,
                        notas_primer_parcial, notas_segundo_parcial, indice,
                        promedios)
                        print("#"*96)
        else:
            print("Error, debe cargar los datos en la opcion 1.")
