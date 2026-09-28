"""
Al ingresar una edad por input, se debe informar si la persona es mayor de edad
(mayor a 17 años) o adolescente (entre 13 y 17 años) o niño (menor a 13 años). 
"""
edad_ingresada = int(input("Ingrese su edad: "))

if edad_ingresada < 13:
    print("Usted es un niño.")

if 13 <= edad_ingresada and edad_ingresada <= 17:
    print("Usted es adolescente.")

else:
    print("Usted es mayor de edad.")