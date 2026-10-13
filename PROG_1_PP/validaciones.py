def es_numero(caracter:str) -> bool:
    """
    Valida si el caracter ingresado es numerico.
    Args: caracter(str)
    Retorno : Booleano
    """ 
    retorno = False
    if 48 <= ord(caracter) <= 57:
        retorno = True

    return retorno

def es_cadena_numerica(cadena:str) -> bool:
    """
    Valida si la cadena ingresada es numerica.
    Args: cadena(str)
    Retorno : Booleano
    """ 
    retorno = True
    for i in cadena:
        valor = es_numero(i)
        if (valor == False):
            retorno = False
            break

    return retorno

def es_alfabetico(caracter:str)-> bool:
    """
    Valida si el caracter ingresado es alfabetico.
    Args: caracter(str)
    Retorno : Booleano
    """ 
    retorno = False
    if (65 <= ord(caracter) <= 90) or (97 <= ord(caracter) <= 122):
        retorno = True
    
    return retorno

def es_cadena_alfa(cadena:str)-> bool:
    """
    Valida si la cadena ingresada es un alfabetica.
    Args: cadena(str)
    Retorno: Booleano
    """
    retorno = True
    for i in cadena:
        valor = es_alfabetico(i)
        if (valor == False):
            retorno = False
            break
    
    return retorno

def validar_genero(genero:str) -> bool:
    """
    Valida el genero ingresado sea f, m o x. Obviando las mayusculas.
    Args: genero(str)
    Retorno: Booleano
    """
    if es_alfabetico(genero):
        match genero:
            case "F" | "f" | "M" | "m" | "X" | "x":
                return True
            case _:
                return False

def validar_nota(nota:str) -> bool:
    """
    Valida que la nota ingresada se encuentre entre el 0 y el 10.
    Args: nota(str)
    Retorno: Booleano
    """
    if nota >= 0 and nota <= 10:
        return True
    else :
        return False
    
def es_num_entero(cadena:str) -> bool:
    """
    Valida si la cadena ingresada es un numero entero.
    Args: cadena(str)
    Retorno : Booleano
    """
    retorno = True
    for i in cadena:
        valor = es_numero(i)
        if (valor == False) and (i != "-"):
            retorno = False
            break

    return retorno



