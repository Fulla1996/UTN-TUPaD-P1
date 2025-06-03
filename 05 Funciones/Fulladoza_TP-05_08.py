def calcular_imc(peso, altura):
    return round(peso / (altura ** 2),2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

print(f"Su IMC es {calcular_imc(peso, altura)}")