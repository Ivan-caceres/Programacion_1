"""
Ingresar cinco (5) números por input, e informar por consola la suma y el promedio
de los números ingresados.

"""
contador = 0
suma = 0
while contador < 5:
    numero = int(input("Ingrese un numero: "))
    suma += numero
    contador += 1
promedio = suma / contador
print(f"La suma de todos los numeros ingresados es: {suma} y el promedio es {promedio}")