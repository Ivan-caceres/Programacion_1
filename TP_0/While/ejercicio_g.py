"""
Ingresar tantos números por input como el usuario desee, e informar por consola la
suma de los números positivos, y la multiplicación de los números negativos.
"""

suma_positivos = 0
mult_negativos = 1
continuar = 'S'
bandera = False

while continuar == 'S' or continuar == 's':
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    if numero >= 0:
        suma_positivos += numero
    else:
        mult_negativos *= numero
        bandera = True

    continuar = input("Desea ingresar otro numero? [S|N]: ")
    
if bandera == False:
    mult_negativos = 0

print(f"La suma de los positivos es: {suma_positivos}, y la multiplicacion de los negativos es: {mult_negativos}.")

