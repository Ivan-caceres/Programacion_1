"""
Al ingresar una edad por input, se debe informar si la persona es adolescente, edad
entre 13 y 17 años (inclusive), caso contrario, no informar nada. 
"""
edad_ingresada = int(input("Ingrese su edad: "))

if 13 <= edad_ingresada and edad_ingresada <= 17:
    print("Usted es adolescente.")