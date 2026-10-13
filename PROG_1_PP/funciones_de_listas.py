def inicializar_listas():
    legajos = []
    nombres = []
    generos = []
    notas_primer_parcial = []
    notas_segundo_parcial = []
    promedios = []

    return legajos, nombres, generos, notas_primer_parcial, notas_segundo_parcial, promedios

def agregar_a_lista(lista:list, elemento:str)->None:
    """
    """
    lista[len(lista): ] = [elemento]

def ordenar_listas(promedio:list,legajos:list, nombres:list, generos:list, notas_primer_parcial:list,
        notas_segundo_parcial:list, orden) -> list:
    """
    """
    n = len(promedio)
    for i in range(n-1):
        for j in range(i+1, n):
            if promedio[j] < promedio[i] and orden == "ASC": #ASC
                promedio[i], promedio[j] = promedio[j], promedio[i]
                legajos[i], legajos[j] = legajos[j], legajos[i]
                nombres[i], nombres[j] = nombres[j], nombres[i]
                generos[i], generos[j] = generos[j], generos[i]
                notas_primer_parcial[i], notas_primer_parcial[j] = notas_primer_parcial[j], notas_primer_parcial[i]
                notas_segundo_parcial[i], notas_segundo_parcial[j] = notas_segundo_parcial[j], notas_segundo_parcial[i]

            elif promedio[j] > promedio[i] and orden == "DES": #DES
                promedio[i], promedio[j] = promedio[j], promedio[i]
                legajos[i], legajos[j] = legajos[j], legajos[i]
                nombres[i], nombres[j] = nombres[j], nombres[i]
                generos[i], generos[j] = generos[j], generos[i]
                notas_primer_parcial[i], notas_primer_parcial[j] = notas_primer_parcial[j], notas_primer_parcial[i]
                notas_segundo_parcial[i], notas_segundo_parcial[j] = notas_segundo_parcial[j], notas_segundo_parcial[i]
    
    return promedio, legajos, nombres, generos, notas_primer_parcial, notas_segundo_parcial


