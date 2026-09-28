"""
Ingresar dos números por input, transformarlos a entero (int).
Luego seleccionar la opción:
Sumar
Restar
Multiplicar
Dividir (numero_uno / numero_dos)
Mostar el resulto por consola.
Ejemplo: "la suma es 750"
"""
numero_uno = int(input("Ingrese el primer numero: "))

numero_dos = int(input("Ingrese el segundo numero: "))

opcion = input("Seleccione el tipo de operacion [suma|resta|multiplicacion|division]: ")
resultado = False

match opcion:
    case "suma":
        resultado = numero_uno + numero_dos
    case "resta":
        resultado = numero_uno - numero_dos
    case "multiplicacion":
        resultado = numero_uno * numero_dos
    case "division":
        if numero_dos != 0:
            division = numero_uno / numero_dos
            resultado = round(division) #redondea los decimales
        else:
            print("No se puede dividir por 0.")
    case _:
        print("No corresponde a una operacion valida.")

if resultado:
    print(f"La {opcion} es {resultado}")