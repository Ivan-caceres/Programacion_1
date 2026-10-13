from validaciones import *

def caracter_mayuscula(caracter:str) -> str:
    
    if es_alfabetico(caracter) and ord(caracter) > 96:
        operacion = ord(caracter) - 32
        caracter_mayus = chr(operacion)
    else:
        caracter_mayus = caracter
    return caracter_mayus 

def cadena_mayuscula(cadena:str) -> str:
    cadena_mayus = ""
    for i in cadena:
        caracter_mayus = caracter_mayuscula(i)
        cadena_mayus = cadena_mayus + caracter_mayus
    return cadena_mayus

def ingresar_num(mensaje:str):
    num_ingresado = input(mensaje)
    while not(es_cadena_numerica(num_ingresado)):
        print("Error! dato invalido.")
        num_ingresado = input(mensaje)

    return num_ingresado

def ingresar_cadena(mensaje:str):
    cadena_valida = input(mensaje)
    while not(es_cadena_alfa(cadena_valida)):
        print("Error! dato invalido.")
        cadena_valida = input(mensaje)

    return cadena_valida

def ingresar_genero(mensaje:str):
    genero_ingresado = input(mensaje)
    while not(validar_genero(genero_ingresado)):
        print("Error! dato invalido.")
        genero_ingresado = input(mensaje)

    return caracter_mayuscula(genero_ingresado)

def ingresar_notas(mensaje:str):
    nota_ingresada = input(mensaje)
    while not(validar_nota(nota_ingresada)):
        print("Error! nota invalida.")
        nota_ingresada = input(mensaje)

    return nota_ingresada

def ingresar_orden(mensaje:str):
    cadena_validada = ingresar_cadena(mensaje)
    while cadena_validada != "ASC" and cadena_validada != "DES" and cadena_validada != "asc" and cadena_validada != "des":
        print("Error! Dato invalido")
        cadena_validada = ingresar_cadena(mensaje)
    
    return cadena_mayuscula(cadena_validada)

def mostrar_estudiante(
        legajos:list, nombres:list, generos:list, notas_primer_parcial:list,
        notas_segundo_parcial:list, indice:int, promedios=None):
    """
    
    """
    if promedios == None:
        print(f"{legajos[indice]}\t\t{nombres[indice]}\t\t\t{generos[indice]}"
        f"\t{notas_primer_parcial[indice]}\t\t\t{notas_segundo_parcial[indice]}")
    else:
        print(f"{legajos[indice]}\t\t{nombres[indice]}\t\t\t{generos[indice]}"
    f"\t{notas_primer_parcial[indice]}\t\t\t{notas_segundo_parcial[indice]}"
    f"\t\t\t{promedios[indice]}")