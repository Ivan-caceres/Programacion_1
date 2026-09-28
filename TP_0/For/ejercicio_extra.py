"""
Ingresar un numero por input y verificar si es un numero primo
"""
numero = int(input("Ingrese un numero: "))
contador = 0

for i in range(1, numero+1):
    es_primo = numero % i
    if es_primo == 0:
        contador += 1
if contador == 2:
    print("El numero es primo")
else:
    print("El numero no es primo")
    