def potencia_recursiva(nro, potencia):
    if potencia == 0:
        return 1
    return nro * potencia_recursiva(nro, potencia - 1)

pot = -1
print("Bienvenido a la calculadora de potencias positivas!")

nro = float(input("Ingrese la base: "))

while pot <= 0:
    pot = int(input(f"Ingrese un número entero positivo para el exponente: "))

print(f"{nro}^{pot} = {potencia_recursiva(nro,pot)}")