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
    Retorno : Booleano
    """
    retorno = True
    for i in cadena:
        valor = es_alfabetico(i)
        if (valor == False):
            retorno = False
            break
    
    return retorno

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

def es_num_real(cadena:str) -> bool:
    """
    Valida si la cadena ingresada es un numero real.
    Args: cadena(str)
    Retorno : Booleano
    """
    retorno = True
    for i in cadena:
        valor = es_numero(i)
        if (valor == False) and (i != ".") and (i != "-"):
            retorno = False
            break
    
    return retorno

