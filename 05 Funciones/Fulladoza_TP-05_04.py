import math
def calcular_area_circulo(radio):
    print(f"El área del circulo es {math.pi * radio**2:.2f}")

def calcular_perimetro_circulo(radio):
    print(f"El perímetro del circulo es {2 * math.pi * radio:.2f}")

radio = float(input("Ingrese el rádio del circulo: "))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)