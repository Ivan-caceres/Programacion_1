"""
Al ingresar una edad por input, solo se debe informar si la persona NO es
adolescente.
"""

edad_ingresada = int(input("Ingrese su edad: "))

if 13 >= edad_ingresada or edad_ingresada >= 17:
    print("Usted no es adolescente.")