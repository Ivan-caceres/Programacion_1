"""
Ingresar un importe por input, transformarlo a número real (float), luego mostrar el
importe ingresado, el 10% del mismo, y el importe con el incremento calculado.
"""
importe = float(input("Ingrese el importe: "))

porcentaje = 0.1 * importe

incremento = porcentaje + importe

print(f"Su importe es {importe}, el 10% es {porcentaje} y el importe incrementado en un 10% es {incremento}.")

