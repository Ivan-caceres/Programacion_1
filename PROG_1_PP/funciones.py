from validaciones import *
from funciones_auxiliares import *

def opciones(primera_opcion:int, ultima_opcion:int) -> int:
    opcion_elegida = input("Elija una opcion: ")
    if es_numero(opcion_elegida):
        opcion = int(opcion_elegida)

        while opcion < primera_opcion or opcion > ultima_opcion:
            print("Error! Opcion invalida")
            opciones(primera_opcion, ultima_opcion)
        return opcion

def pedir_str(mensaje:str, num_o_alfa:str):
    dato = input(mensaje)
    if num_o_alfa == "NUM" and es_cadena_numerica(dato):
        return dato
    elif num_o_alfa == "ALFA" and es_cadena_alfa(dato):
        return dato
    else:
        print("Error!, dato invalido.")
        pedir_str(mensaje, num_o_alfa)
        

def realizar_carga():

    legajos = []
    nombres = []
    generos = []
    notas_primer_parcial = []
    notas_segundo_parcial = []
    
    legajo_ingresar = pedir_str("Ingese el numero de legajo: ", "NUM")
    agregar_a_lista(legajos, legajo_ingresar)

    nombre_ingresar = pedir_str("Ingrese el nombre del estudiante: ", "ALFA")
    agregar_a_lista(nombres, nombre_ingresar)

    generos_ingresar = pedir_str("Ingrese el genero del estudiante [F/M/X]: ", "ALFA")
    while validar_genero(generos_ingresar):
        print("Error! opcion invalida.")
        generos_ingresar = pedir_str("Ingrese el genero del estudiante [F/M/X]: ", "ALFA")
    agregar_a_lista(generos, generos_ingresar)

    notas_primer_parcial_ingresar = pedir_str("Ingrese la nota del primer parcial: ", "NUM")
    while validar_nota(notas_primer_parcial_ingresar):
        print("Error! nota invalida.")
        notas_primer_parcial_ingresar = pedir_str("Ingrese la nota del primer parcial: ", "NUM")
    agregar_a_lista(notas_primer_parcial, notas_primer_parcial_ingresar)

    notas_segundo_parcial_ingresar = pedir_str("Ingrese la nota del segundo parcial: ", "NUM")
    while validar_nota(notas_segundo_parcial_ingresar):
            print("Error! nota invalida.")
            notas_segundo_parcial_ingresar = pedir_str("Ingrese la nota del primer parcial: ", "NUM")
    agregar_a_lista(notas_segundo_parcial, notas_segundo_parcial_ingresar)
    
def mostrar_datos():
    pass

def calcular_promedio():
    pass

def mostrar_datos_ord(orden:str):
    pass

def mostrar_mayor_prom():
    pass

def buscar_estudiantes_legajo(legajo:str):
    pass