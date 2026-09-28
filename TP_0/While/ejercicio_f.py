"""
Ingresar tantos números por input como el usuario desee, e informar por consola la
suma y el promedio de los números ingresados.
"""
bandera = True
suma = 0
contador = 0
while bandera:
    numero = int(input("Ingrese un numero: "))
    suma += numero
    contador += 1
    opcion = input("Desea ingresar otro numero? [S/N]: ")
    if opcion == "n" or opcion == "N":
        bandera = False
    elif opcion != "s" or opcion != "S":
        print("Opcion invalida.")
promedio = suma / contador
print(f"La suma de todos los numeros ingresados es: {suma} y el promedio es {promedio}")