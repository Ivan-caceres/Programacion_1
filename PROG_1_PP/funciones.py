from validaciones import *
from funciones_auxiliares import *
from funciones_de_listas import *

def opciones(primera_opcion:int, ultima_opcion:int) -> int:
    opcion_elegida = input("Elija una opcion: ")
    if es_cadena_numerica(opcion_elegida):
        opcion = int(opcion_elegida)

        while opcion < primera_opcion or opcion > ultima_opcion:
            print("Error! Opcion invalida")
            opciones(primera_opcion, ultima_opcion)
        return opcion

def realizar_carga(legajos:list, nombres:list, generos:list,
                    notas_primer_parcial:list, notas_segundo_parcial:list):
    """
    """
    print("Ingrese los datos del estudiante.")
    
    legajo_ingresado = ingresar_num("Ingrese el numero de legajo: ")
    agregar_a_lista(legajos, legajo_ingresado)

    nombre_ingresado = ingresar_cadena(
        "Ingrese el nombre del estudiante: ")
    agregar_a_lista(nombres, nombre_ingresado)

    genero_ingresado = ingresar_genero(
        "Ingrese el genero del estudiante [F|M|X]: ")
    agregar_a_lista(generos, genero_ingresado)

    nota_primer_parcial_ingresado = ingresar_notas(
        "Ingrese la nota del primer parcial: ")
    agregar_a_lista(notas_primer_parcial, nota_primer_parcial_ingresado)

    nota_segundo_parcial_ingresado = ingresar_notas(
        "Ingrese la nota del segundo parcial: ")
    agregar_a_lista(notas_segundo_parcial, nota_segundo_parcial_ingresado)

    return legajos, nombres, generos, notas_primer_parcial, notas_segundo_parcial
    
def mostrar_datos(
        legajos:list, nombres:list, generos:list, 
        notas_primer_parcial:list, notas_segundo_parcial:list, promedios =None):
    """
    """
    if promedios == None:
        print("#"*96)
        print("\t\t\t\t\tLISTADO DE ESTUDIANTES")
        print("#"*96)
        print("Nro Legajo\tNombre del estudiante\t\tGenero\tNota 1er parcial\t"
        "Nota 2do parcial")
        for i in range(len(legajos)):
            mostrar_estudiante(legajos, nombres, generos, notas_primer_parcial,
                        notas_segundo_parcial, i)
        print("#"*96)
    else:
        print("#"*96)
        print("\t\t\t\t\tLISTADO DE ESTUDIANTES")
        print("#"*96)
        print("Nro Legajo\tNombre del estudiante\t\tGenero\tNota 1er parcial\t"
        "Nota 2do parcial\tPromedios")
        for i in range(len(legajos)):
            mostrar_estudiante(legajos, nombres, generos, notas_primer_parcial,
            notas_segundo_parcial, i, promedios)
        print("#"*96)

def calcular_promedio(
        notas_primer_parcial:list, notas_segundo_parcial:list, promedios:list):
    """
    """
    for i in range(len(notas_primer_parcial)):
        suma = float(notas_primer_parcial[i]) + float(notas_segundo_parcial[i])
        promedio =  suma / 2
        agregar_a_lista(promedios, round(promedio, 2))
    
def encontrar_mayor_prom(promedio:list) -> int:
    """
    
    """
    for i in range(len(promedio)):
        if i == 0:
            indice_maximo = i
            maximo = promedio[i]
        
        if promedio[i] > maximo:
            indice_maximo = i
            maximo = promedio[i] 

    return indice_maximo


def buscar_estudiantes_legajo(legajo:list, numero:str):
    """
    """
    indice_encontrado = None
    for i in range(len(legajo)):
        if legajo[i] == numero:
            indice_encontrado = i
    if indice_encontrado != None:
        return indice_encontrado
    else:
        print("Legajo no encontrado.")
