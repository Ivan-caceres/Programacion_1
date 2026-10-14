from validaciones import *

def caracter_mayuscula(caracter:str) -> str:
    """
    Pasa a mayuscula el caracter ingresado.

    Args: caracter(str)
    
    Retorno: caracter_mayus(str)
    """
    if es_alfabetico(caracter) and ord(caracter) > 96:
        operacion = ord(caracter) - 32
        caracter_mayus = chr(operacion)
    else:
        caracter_mayus = caracter
    return caracter_mayus 

def cadena_mayuscula(cadena:str) -> str:
    """
    Pasa a mayuscula la cadena ingresado.
    
    Args: cadena(str)
        
    Retorno: cadena_mayus(str)
    """
    cadena_mayus = ""
    for i in cadena:
        caracter_mayus = caracter_mayuscula(i)
        cadena_mayus = cadena_mayus + caracter_mayus
    return cadena_mayus

def ingresar_num(mensaje:str) -> str:
    """
    Valida el ingreso de una cadena numerica y la retorna.

    Args: mensaje(str)

    Retorno: num_ingresado(str)
    """
    num_ingresado = input(mensaje)
    while not(es_cadena_numerica(num_ingresado)):
        print("Error! dato invalido.")
        num_ingresado = input(mensaje)

    return num_ingresado

def ingresar_cadena(mensaje:str) -> str:
    """
    Valida el ingreso de una cadena alfabetica y la retorna.

    Args: mensaje(str)

    Retorno: cadena_valida(str)
    """
    cadena_valida = input(mensaje)
    while not(es_cadena_alfa(cadena_valida)):
        print("Error! dato invalido.")
        cadena_valida = input(mensaje)

    return cadena_valida

def ingresar_genero(mensaje:str) -> str:
    """
    Valida el ingreso de un genero y lo retorna en mayusculas.

    Args: mensaje(str)

    Retorno: genero_mayus(str)
    """
    genero_ingresado = input(mensaje)
    while not(validar_genero(genero_ingresado)):
        print("Error! dato invalido.")
        genero_ingresado = input(mensaje)
    genero_mayus = caracter_mayuscula(genero_ingresado)

    return genero_mayus

def ingresar_notas(mensaje:str) -> str:
    """
    Valida el ingreso de una nota y la retorna.

    Args: mensaje(str)

    Retorno: nota_ingresada(str)
    """
    nota_ingresada = input(mensaje)
    while not(validar_nota(nota_ingresada)):
        print("Error! nota invalida.")
        nota_ingresada = input(mensaje)

    return nota_ingresada

def ingresar_orden(mensaje:str) -> str:
    """
    Valida el ingreso del orden ASC o DES y lo retorna en mayusculas.

    Args: mensaje(str)

    Retorno: cadena_mayus(str)
    """
    cadena_validada = ingresar_cadena(mensaje)
    while cadena_validada != "ASC" and cadena_validada != "DES" and cadena_validada != "asc" and cadena_validada != "des":
        print("Error! Dato invalido")
        cadena_validada = ingresar_cadena(mensaje)
    cadena_mayus = cadena_mayuscula(cadena_validada)
    
    return cadena_mayus

def mostrar_estudiante(
        legajos:list, nombres:list, generos:list, notas_primer_parcial:list,
        notas_segundo_parcial:list, indice:int, promedios=None):
    """
    Muestra los datos del estudiante con formato.

    Args: legajos(list), nombres(list), generos(list), 
    notas_primer_parcial(list), notas_segundo_parcial(list), promedio(list)
    """
    if promedios == None:
        print(f"{legajos[indice]}\t\t{nombres[indice]}\t\t\t{generos[indice]}"
        f"\t{notas_primer_parcial[indice]}\t\t\t{notas_segundo_parcial[indice]}")
    else:
        print(f"{legajos[indice]}\t\t{nombres[indice]}\t\t\t{generos[indice]}"
    f"\t{notas_primer_parcial[indice]}\t\t\t{notas_segundo_parcial[indice]}"
    f"\t\t\t{promedios[indice]}")