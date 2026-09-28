"""
Ingresar por input un número, convertirlo a entero (int), y mostrar por consola todos
los números impares desde 1 hasta el número ingresado.
"""
numero = int(input("Ingrese un numero: "))

for i in range (1, numero + 1):
    es_par = i % 2 
    if es_par != 0:
        print(i)
    