"""
Ingresar dos números por input, transformarlos a enteros (int), realizar la operación
aritmética de división, pero para obtener y mostrar el resto (operador módulo) entre
el dividendo (numero_uno) y el divisor (numero_dos).
Ejemplo: "El resto es 0."
"""
numero_uno = int(input("Ingrese el dividendo: "))

numero_dos = int(input("Ingrese el divisor: "))

resto = numero_uno % numero_dos

print(f"El resto es {resto}")