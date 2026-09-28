"""
Ingresar un número por input, y mostrarlo por consola. El número ingresado debe
estar comprendido entre 0 y 9 inclusive, caso contrario volver a pedirlo hasta que el
número ingresado esté dentro de ese rango.
"""
bandera = True
while bandera:
    numero = int(input("Ingrese un numero: "))
    if 0 <= numero <= 9:
        bandera = False