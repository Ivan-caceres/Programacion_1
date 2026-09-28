"""
Al ingresar una edad por input se debe informar si la persona es mayor de edad,
caso contrario, informar que es un menor de edad. 
"""
edad_ingresada = int(input("Ingresar su edad: "))

if edad_ingresada >= 18:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")