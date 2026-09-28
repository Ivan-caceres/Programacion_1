"""
Ingresar un importe por input, transformarlo a número real (float), luego mostrar el
importe ingresado, el 25% del mismo, y el importe con el descuento calculado.
"""

importe = float(input("Ingrese el importe: "))

porcentaje = 0.25 * importe

decremento = importe - porcentaje

print(f"Su importe es {importe}, el 25% es {porcentaje} y el importe decrementado en un 25% es {decremento}.")
