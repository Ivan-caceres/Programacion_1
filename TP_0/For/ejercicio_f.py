"""
Ingresar por input un número mayor a 0 (cero), y mostrar ese número por consola.
Repetir la operación una y otra vez, hasta que ingresemos (cero), en ese caso
finalizar la ejecución del programa.
"""
for _ in iter(int, 1):
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        break
    elif numero > 0:
        print(numero)
    